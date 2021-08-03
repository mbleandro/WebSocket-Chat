<template>
  <v-layout justify-center align-center>
    <chat-atendimento v-if="chat=='ATENDIMENTO'" color="success" :to="{name: 'todos'}" />
    <chat-grupo v-if="chat=='GRUPO'" color="error" :to="{name: 'todos'}" />
  </v-layout>
</template>

<script>
import chatAtendimento from '~/components/chat-atendimento'
import chatGrupo from '~/components/chat-grupo.vue'

export default {
  components: {
    chatAtendimento,
    chatGrupo
  },
  data () {
    return {}
  },
  mounted () {
    console.log('AAAAAAA')
  },
  computed: {
    user () {
      return this.$store.state.chat.user
    },
    chat () {
      return this.$store.state.chat.chat
    }
  }
}
</script>

<style>
</style>
