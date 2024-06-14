<template>
  <div class="home">
    <vue-html2pdf
        :show-layout=showLayout
        :float-layout="true"
        :enable-download="true"
        :preview-modal="true"
        :paginate-elements-by-height="1400"
        filename="我是pdf"
        :pdf-quality="2"
        :manual-pagination="false"
        pdf-format="a4"
        pdf-orientation="landscape"
        pdf-content-width="800px"
        :html-to-pdf-options="htmlToPdfOptions"

        @progress="onProgress($event)"
        @hasStartedGeneration="hasStartedGeneration()"
        @hasGenerated="hasGenerated($event)"
        ref="html2Pdf"
    >
      <section slot="pdf-content">
        <img alt="Vue logo" src="../assets/logo.png">
        <PdfPrint msg="Welcome to Your Vue.js App"/>
        <a href="https://www.baidu.com">https://www.baidu.com</a>
      </section>
    </vue-html2pdf>
    <div class="display-flex control-container">
      <div>
        <button v-on:click="show">Switch</button>
      </div>
      <div>
        <button v-on:click="generateReport">Get PDF</button>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import PdfPrint from '@/components/PdfPrint.vue'
import VueHtml2pdf from 'vue-html2pdf'

export default {
  name: 'Pdf',
  data() {
    return {
      name: 'Vue.js',
      showLayout: true
    }
  },
  computed: {
    htmlToPdfOptions() {
      return {
        margin: 0,

        filename: "我是pdf.pdf",

        image: {
          type: "jpeg",
          quality: 0.98,
        },

        enableLinks: true,

        html2canvas: {
          scale: 2,
          useCORS: true,
        },

        jsPDF: {
          unit: "in",
          format: 'a4',
          orientation: 'portrait',
        },
      };
    },
  },
  methods: {
    show: function(){
      this.showLayout = !this.showLayout
    },
    greet: function (event) {
      // `this` inside methods points to the Vue instance
      alert('Hello ' + this.name + '!')
      // `event` is the native DOM event
      if (event) {
        alert(event.target.tagName)
      }
    },
    generateReport () {
      this.$refs.html2Pdf.generatePdf()
    }
  },
  components: {
    PdfPrint,
    VueHtml2pdf
  }
}
</script>
<style scoped>
.control-container {
  position: fixed;
  z-index: 999999;
}
.display-flex {
  display: flex;
}
</style>


