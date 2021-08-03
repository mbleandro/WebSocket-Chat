<template>
  <v-card class="chat">
    <v-list two-line class="list">
      <template v-for="message in messages">
        <v-list-item :key="message.title" class="bottom-dooted-line">
          <div class="avatar-box">
            <v-img class="avatar" :src="message.avatar"></v-img>
          </div>
          <div class="message">
            <div class="message-head">
              <div>{{ message.name }}</div>
              <div class="message-time">{{ message.message.time }}</div>
            </div>
            <div class="message-text">
              <div>{{ message.message.text }}</div>
            </div>
          </div>
        </v-list-item>
      </template>
    </v-list>
    <v-card-actions>
      <v-text-field
        v-if="user"
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
export default {
  data () {
    return {
      messages: [],
      teste: 'sadasdasdasdasdasdasd',
      new_message_text: '',
      connection: null,
      link: null
    }
  },
  mounted () {
    api.list_group_messages().then((result) => {
      this.messages = result.messages
      this.link = result.link
      this.make_connection(this.link)
    })
  },
  computed: {
    user () {
      return this.$store.state.chat.user
    }
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
    async send_message (evt) {
      if (this.new_message_text.length > 0) {
        // api.send_message({
        //   avatar: this.user.avatar,
        //   name: this.user.name,
        //   message: this.new_message_text
        // })
        // this.new_message_text = ''
        const data = new Date()
        const datastr = `${data.getDate()}/${data.getMonth()}/${data.getFullYear()} ${data.getHours()}:${data.getMinutes()}`
        const new_message = {
          avatar: this.user.avatar,
          name: this.user.name,
          message: {text: this.new_message_text, time: datastr}
        }
        await this.connection.send(JSON.stringify({
          'message': new_message,
          'type': 'GRUPO',
          'user_id': this.user.id
        }))
        this.new_message_text = ''
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
  margin-right: 20px;
  border-radius: 100%;
}

.list {
  overflow-y: scroll;
  height: 430px;
}

.message {
  display: flex;
  flex-direction: column;
}

.message-user {
  color: white;
}

.message-head {
  color: gray;
  display: flex;
}

.message-time {
  font-size: 10px;
  margin-left:10px;
  margin-top: 8px;
}

.message-box {
  width: 100%;
  background-color: gray;
}

.avatar-box {
  margin-left: 20px;
}

.bottom-dooted-line {
  border-bottom: 0.5px dotted gray;
}
</style>
