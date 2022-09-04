<script>
    
    // RELEVANT: https://kit.svelte.dev/faq

    // TODO
    // the plan here was to let the user click on the clock panel to expand to seconds or collapse
    // back into minutes, im just kinda lazy and it takes a lot of screen realestate so can just leave it
    // as minutes for now

    // get clock mode from local storage
    // var mode = window.localStorage.getItem('clockmode');
    // // if clock mode doesent exist set it to minutes
    // if(mode === null){
    //     window.localStorage.setItem('clockmode','minutes')
    // }

    // declare our time variable (starts as placeholder)
    var time = '00:00'

    // declare function for getting the time and setting it based on the mode
    function gettime(){
        var date = new Date(); // get current datetime
        var hours = date.getHours(); // extract hours from datetime
        var minutes = date.getMinutes(); //extract minutes from datetime
        // var seconds = (date.getMinutes() < 10 ? '0' : '') + date.getMinutes(); bugged ass method for getting seconds
        var ampm = hours >= 12 ? 'pm' : 'am'; // decipher whether its AM or PM
        hours = hours % 12; // some other code i copy pasted
        hours = hours ? hours : 12; // the hour '0' should be '12'
        minutes = minutes < 10 ? '0'+minutes : minutes; // more code i copy pasted etc etc
        var strTime = hours + ':' + minutes + ' ' + ampm; // build final locale string
        // if(mode == 'seconds'){
        //     var strTime = hours + ':' + minutes + ':' + seconds + ' ' + ampm;
        // }
        // else{
        //     var strTime = hours + ':' + minutes + ' ' + ampm;
        // } bugged seconds time
        time = strTime;
        setTimeout(gettime,1000);
    }
    gettime();
</script>
<main>
    <div class="clock bg3">
        <p class="clocktxt">{time}</p>
    </div>
</main>
<style>
    .clock{
        border-radius: 15px;
        margin-right: 10px;
    }
    .clocktxt{
        padding: 5px;
        font-size: 25px;
    }
</style>