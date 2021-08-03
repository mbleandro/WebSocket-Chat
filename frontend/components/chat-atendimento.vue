<template>
  <v-card class="chat">
    <div v-if="!error" class="encerra-atendimento">
      <v-btn depressed @click="encerrar_atendimento()">
        ENCERRAR
      </v-btn>
    </div>
    <div v-if="error" style="width: 100%; align-text: center;">
      {{error}}
    </div>
    <v-list two-line class="list" v-if="!error">
      <template v-for="(message, index) in messages" style="display-flex">
        <v-list-item :key="index" avatar :style="message.remetente == user_type ? 'justify-content: flex-end;' : ''">
          <v-list-tile-content>
            <div class="message">
              <div class="message-head">
                <div>{{ message.remetente }}</div>
                <div class="message-time">{{ message.time }}</div>
              </div>
              <div class="message-text">
                <div>{{ message.text }}</div>
              </div>
            </div>
          </v-list-tile-content>
        </v-list-item>
      </template>
    </v-list>
    <v-card-actions v-if="!error">
      <v-text-field
        v-model="new_message_text"
        solo
        v-on:keyup.enter="send_message($event)"
        class="message-box"
        placeholder="Mensagem"
      />
    </v-card-actions>
  </v-card>
</template>

<script>
import api from '~api'
import Snacks from '~/helpers/Snacks.js'
export default {
  data () {
    return {
      messages: [],
      new_message_text: '',
      atendimento_id: null,
      error: null
    }
  },
  computed: {
    user_type () {
      return this.$store.state.chat.user_type
    },
    user () {
      return this.$store.state.chat.user
    }
  },
  mounted () {
    api.list_atendimento_messages().then((result) => {
      if (result.error) {
        this.error = result.error
      } else {
        this.messages = result.messages
        this.link = result.link
        this.atendimento_id = result.id
        this.make_connection(this.link)
      }
    })
  },
  methods: {
    make_connection (link) {
      this.connection = new WebSocket(link)
      const self = this
      this.connection.onmessage = function (event) {
        const message = JSON.parse(event.data)
        self.messages.push(JSON.parse(message.message))
      }
      this.connection.onopen = function (event) {
        console.log(event)
        console.log('Successfully connected to the echo websocket server...')
      }
      this.connection.onerror = function (event) {
        console.log(event)
      }
    },
    encerrar_atendimento () {
      api.encerra_atendimento(this.atendimento_id).then(() => {
        this.$store.commit('chat/SET_CHAT_GRUPO')
        Snacks.show(this.$store, {text: 'Atendimento Fechado!'})
        this.connection.close()
      })
    },
    async send_message (evt) {
      if (this.new_message_text.length > 0) {
        const new_message = {
          message: this.new_message_text
        }
        this.new_message_text = ''
        await this.connection.send(JSON.stringify({
          'message': new_message,
          'type': 'ATENDIMENTO',
          'id': this.atendimento_id,
          'user_id': this.user.id
        }))
      }
    }
  }
}
</script>

<style>
.chat {
  width: 90%;
}

.avatar {
  width: 40px;
  height: 40px;
  margin-right: 30px;
  border-radius: 100%;
}

.list {
  overflow-y: scroll;
  height: 430px;
}

.alinha-esquerda {
  display: flex;
  align-items: flex-end;
}

.alinha-direita {
  align-items: right;
}

.message-box {
  width: 100%;
  background-color: gray;
}

.encerra-atendimento {
  width: 100%;
  display: flex;
  justify-content: flex-end;
}
</style>
