<script>
    const passage = "Google LLC is an American multinational technology company that specializes in Internet-related services and products, which include online advertising technologies, search engine, cloud computing, software, and hardware. It is considered one of the Big Four technology companies, alongside Amazon, Apple, and Facebook. Google was founded in September 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a California privately held company on September 4, 1998, in California. Google was then reincorporated in Delaware on October 22, 2002. An initial public offering (IPO) took place on August 19, 2004, and Google moved to its headquarters in Mountain View, California, nicknamed the Googleplex. In August 2015, Google announced plans to reorganize its various interests as a conglomerate called Alphabet Inc. Google is Alphabet's leading subsidiary and will continue to be the umbrella company for Alphabet's Internet interests. Sundar Pichai was appointed CEO of Google, replacing Larry Page who became the CEO of Alphabet.";
    
    let inputText = 'Talk with Cortana here.';
    let answerText = 'Cortana will answer you here';

    let answerIndex = 0;

    function OnAnswer(answers) {
        alert(answers);
    }

    function OnInput() {
        if (answerIndex == 1) answerText = "I'm sorry, you have to repeat that.";
        answerIndex ++;
    }

 </script>
 
 <div class="">
    <h2 class="card-text">Cortana</h2>
    <div class="form-group">
        <label>🖊 Write here:</label>
        <input type="text" name="title" class="form-control" bind:value={inputText} on:change={console.log("input control: " + answerIndex)}>
        <span class="invalid-feedback">Dab on the haters</span>
        <p>{answerText}</p>
    </div>
</div>

<div passage="{passage}" question="{inputText}" on:answers="{OnAnswer}" />
    
<style>

</style>