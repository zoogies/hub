<script>
    import Loading from "../../lib/Loading.svelte";
    import axios from 'axios';
    import { onMount } from 'svelte';
  import Button from "../../lib/Button.svelte";
    
    var loaded = false;
    var error = true;
    var models = [];
    const ip = 'https://zoogies.live'
    var buttonlabel = "Complete"
    
    let selectedModel = {};

    async function fetchModels() {
        try {
            const response = await axios.get(`${ip}/api/completion/models`);
            models = response.data.models;
            selectedModel = models[0]; // Set the first model as the selected one
            error = false;
        } catch (err) {
            console.error(err);
            error = true;
        } finally {
            loaded = true;
        }
    }

    let text = '';
    let requesting = false;
    async function completion() {
        try {
            if(text.length >= 1){
                if(!requesting){
                    requesting = true;
                    buttonlabel = "Completing..."
                    const formData = new FormData();
                    formData.append("prompt", text);
                    formData.append("max_length", sliderValueLength);
                    formData.append("temperature", sliderValueTemp);
                    formData.append("top_p", sliderValueTopP);

                    const response = await axios.post(`${ip}/api/completion`, formData, {
                        headers: { "Content-Type": "multipart/form-data" },
                    });
                    
                    if (response.data.hasOwnProperty("error")) {
                        // Handle the error case
                        console.error(response.data.error);
                        text = 'ERROR:\n'+response.data.error
                    } else {
                        // Handle the success case
                        buttonlabel = "Complete"
                        text = response.data.generated_text;
                    }
                    requesting = false;
                }
                
            }
            else{
                alert("Please enter at least one character.")
            }
        }
        catch (error) {
            console.error('Error:', error);
        }
            
    }

    onMount(() => {
        fetchModels();
    });

    const handleModelSelect = (event) => {
        selectedModel = models[event.target.selectedIndex];
    };


    let sliderValueTemp = .7;
    let sliderValueTopP = 1;
    let sliderValueLength = 200;

    const syncValueTemp = (event) => {
        const value = Math.min(Math.max(event.target.value, 0), 1);
        sliderValueTemp = value;
    };

    const syncValueTopP = (event) => {
        const value = Math.min(Math.max(event.target.value, 0), 1);
        sliderValueTopP = value;
    };

    const syncValueLength = (event) => {
        const value = Math.min(Math.max(event.target.value, 0), 300);
        sliderValueLength = value;
    };

</script>

<main>
    {#if !loaded}
        <Loading/>
    {:else}
        <div class="page_top">
            <div class="playground_top">
                {#if error}
                    <div class="error-fit">
                        <h1 style="color: red;">Server is offline</h1>
                        <p style="color: gray;">If you are seeing this message, something is seriously wrong ;-;</p>
                    </div>
                {:else}
                    <div class="bg2 playground_sidebar playground_panel shadow">
                        <p class="label">Model:</p>
                        <select on:change="{handleModelSelect}">
                            {#each models as model, index (model.name)}
                                <option value="{model.name}" selected="{index === 0}">{model.name}</option>
                            {/each}
                        </select>
                        <p>{selectedModel.description}</p>
                
                <p class="label">Temperature:</p>
                <div class="slider-container">
                    <input
                      type="range"
                      class="slider_grow"
                      step=.01
                      bind:value="{sliderValueTemp}"
                      min=".01"
                      max="1"
                      on:input="{syncValueTemp}"
                    />
                    <input
                      type="number"
                      class="num_input"
                      bind:value="{sliderValueTemp}"
                      min=".01"
                      max="1"
                      on:input="{syncValueTemp}"
                    />
                  </div>

                <p class="label">Top P:</p>
                <div class="slider-container">
                    <input
                      type="range"
                      class="slider_grow"
                      step=.01
                      bind:value="{sliderValueTopP}"
                      min=".01"
                      max="1"
                      on:input="{syncValueTopP}"
                    />
                    <input
                      type="number"
                      class="num_input"
                      bind:value="{sliderValueTopP}"
                      min=".01"
                      max="1"
                      on:input="{syncValueTopP}"
                    />
                  </div>

                <p class="label">Maximum Length:</p>
                <div class="slider-container">
                    <input
                    type="range"
                    class="slider_grow"
                    step=1
                    bind:value="{sliderValueLength}"
                    min="1"
                    max="300"
                    on:input="{syncValueLength}"
                    />
                    <input
                    type="number"
                    class="num_input"
                    bind:value="{sliderValueLength}"
                    min="1"
                    max="300"
                    on:input="{syncValueLength}"
                    />
                </div>

                <button on:click="{completion}">{buttonlabel}</button>
                <!-- TODO change complete to thinking or loading or give some loading indicator while the client is waiting for the completion, also a timeout -->
            </div>
    
            <div class="bg2 playground_input playground_panel shadow">
                <textarea bind:value="{text}" placeholder="Enter text to be completed"></textarea>
            </div>
            
    {/if}
    </div>
</div> 
{/if}
<!-- TODO ADD A LITTLE YELLOW WARNING AT THE BOTTOM THAT THE MODELS OFTEN GENERATE NOTHING IF THEY DO NOT END ON A WORD THAT IMPLIES A CONTINUATION -->
</main>
<style>

.page_top{
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
}

.playground_top{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    max-width: 1500px;
    width: 100%;
    height: 100%;
}

.playground_panel{
    margin: 20px;
    border-radius: 9px;
}

.playground_sidebar{
    min-width: 330px;
    display: flex;
    flex-direction: column;
    padding: 10px;
    max-width: 400px;
}

.playground_input{
    padding: 10px;
    min-width: 300px;
    flex-grow: 4;
    min-height: 300px;
}

textarea {
    width: 100%;
    height: 100%;
    outline: none;
    border: none;
    resize: none;
    box-sizing: border-box;
    padding: 10px;
    font-size: 16px;
    color: white;
    font-family: 'Poppins', sans-serif;
    background-color: #212121;
}

select{
    color: white;
    font-family: 'Poppins', sans-serif;
    background-color: #212121;
}

button{
    background-color: green;
    color: white;
    font-family: 'Poppins', sans-serif;
    height: 40px;
    border-radius: 10px;
    font-size: large;
    font-weight: 400;
    margin-top:auto;
}

.label{
    font-weight: 400;
    margin: 0px;
    margin-top: 0px;
    margin-bottom: 5px;
}

.model_select{
    margin-bottom: 10px;
}

.slider-container {
display: flex;
align-items: center;
margin-bottom: 10px;
}

input[type="number"] {
margin-left: 1rem;
width: 4rem;
}

.slider_grow{
    flex-grow: 4;
    accent-color: white;
    background-color: #212121;
}

.num_input{
    background-color: #212121;
    color: white;
    font-family: 'Poppins', sans-serif;
}

/* Chrome, Safari, Edge, Opera */
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

</style>