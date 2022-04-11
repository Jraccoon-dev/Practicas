<template>
<div v-if="showName"><p>{{user.first_name}}</p></div>
<div v-else><p>No set Name</p></div>
</template>

<script>
export default{
  data () {
    return {
      title: 'Hola VueJs',
      user: {
        first_name: 'Jose',
        last_name: 'McMilan'
      },
      myHtml: '<h1>Hola Barco </h1>',
      showName: false
    }
  }
}
</script>

<style media="screen">
</style>
