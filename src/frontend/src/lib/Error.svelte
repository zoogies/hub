<script>
    export let message;
    export let description;
</script>

<div class="error-fit">
    <h1 style="color: red;">{message}</h1>
    <p style="color: gray;">{description}</p>
</div>

<style>
    .error-fit{
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        text-align: center;
        margin: 100px;
        margin-top: 50px;
    }
    .error-fit > h1 {
        margin: 0px;
    }
    .error-fit > p {
        margin: 0px;
    }
</style>