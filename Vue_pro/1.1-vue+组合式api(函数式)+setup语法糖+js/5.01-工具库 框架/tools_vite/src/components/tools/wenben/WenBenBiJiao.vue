<script setup>
import { onMounted, ref } from "vue";

const textA = ref(null);
const textB = ref(null);
const resultC = ref(null);
const resultD = ref(null);
const resultE = ref(null);

onMounted(() => {
    textA.value.value="1\n2\n3"
    textB.value.value="3\n4\n\n5"

    document.getElementById('calculate').addEventListener('click', () => {
        const textAValue = textA.value.value;
        const textBValue = textB.value.value;

        const setA = new Set(textAValue.split('\n').map(line => line.trim()).filter(line => line !== ''));
        const setB = new Set(textBValue.split('\n').map(line => line.trim()).filter(line => line !== ''));

        const setC = new Set([...setA].filter(x => !setB.has(x)));
        const setD = new Set([...setA].filter(x => setB.has(x)));
        const setE = new Set([...setB].filter(x => !setA.has(x)));

        resultC.value.value = [...setC].join('\n');
        resultD.value.value = [...setD].join('\n');
        resultE.value.value = [...setE].join('\n');
    });
});

</script>

<template>
<div class="yeye">
    <div>
        <label for="textA">文本 A:</label><br>
        <textarea ref="textA"></textarea>
    </div>
    <div>
        <label for="textB">文本 B:</label><br>
        <textarea ref="textB"></textarea>
    </div>
    <button id="calculate">计算</button>
    <div>
        <label for="resultC">A独有:</label><br>
        <textarea ref="resultC" readonly></textarea>
    </div>
    <div>
        <label for="resultD">AB交集:</label><br>
        <textarea ref="resultD" readonly></textarea>
    </div>
    <div>
        <label for="resultE">B独有:</label><br>
        <textarea ref="resultE" readonly></textarea>
    </div>
</div>
</template>

<style>
.yeye {
    display: flex;
    justify-content: center;
}

textarea {
    width: 300px;
    height: 300px;
}
#result {
    width: 300px;
    height: 300px;
}
</style>