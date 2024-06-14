<template>
  <div class="home">
    <div class="display-flex control-container">
      <div>
        <button v-on:click="login">Login</button>
        <button v-on:click="getFile">Get File</button>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
const axios = require('axios').default;
const streamSaver = require('streamsaver');

export default {
  name: 'Download',
  data() {
    return {
      name: 'Vue.js',
      url: 'hello'
    }
  },
  methods: {
    login: function () {
      const data = JSON.stringify({
        "account": "xxx",
        "password": "xxxx"
      });

      const config = {
        method: 'post',
        url: '/api/login',
        headers: {
          'Content-Type': 'application/json'
        },
        data: data
      };

      axios(config)
          .then(function (response) {
            console.log(JSON.stringify(response.data));
          })
          .catch(function (error) {
            console.log(error);
          });
    },
    getFile: function () {

      const url = '/api/common/downloadFile?xxxx.srt'

      fetch(url, {
        method: 'GET',
        cache: 'no-cache',
        headers: {
          'xxxx': 'xxxx'
        }
      }).then(res => {

        const fileStream = streamSaver.createWriteStream('xxxx.srt', {
          size : res.headers.get("content-length")
        })

        const readableStream = res.body

        // more optimized
        if (window.WritableStream && readableStream.pipeTo) {
          return readableStream.pipeTo(fileStream)
              .then(() => console.log('done writing'))
        }
        window.writer = fileStream.getWriter()

        const reader = res.body.getReader()
        const pump = () => reader.read()
            .then(res => res.done
                ? window.writer.close()
                : window.writer.write(res.value).then(pump))

        pump()
      })


    }
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


