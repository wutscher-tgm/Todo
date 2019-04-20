<template>
    <div>
        <span v-html="convertedHTML"></span>
    </div>
</template>
<script>
export default {
    name: 'md',
    props: ['data'],
    data(){
        return {
            convertedHTML: null
        }
    },
    methods: {
        convert(){
            const showdown = require('showdown')
            const showdownHighlight = require("showdown-highlight")
            
            let converter = new showdown.Converter({
                extensions: [showdownHighlight]
            });
            
            let html = converter.makeHtml(this.data);
            
            console.log(html);
            return html
        }
    },
    created(){
        this.convertedHTML = this.convert()
    }
}
</script>
<style lang="scss">

</style>

