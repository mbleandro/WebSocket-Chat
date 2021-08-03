import { zuck } from './db_people'
import { todos } from './db_todos'
import { mockasync } from './mockutils'

const keepLoggedIn = true

export default {
  login (username, password) {
    return mockasync(zuck)
  },
  logout () {
    return mockasync({})
  },
  whoami () {
    const iam = { authenticated: keepLoggedIn }
    if (iam.authenticated) {
      iam.user = zuck
    }
    return mockasync(iam)
  },
  settings () {
    return mockasync({
      SENTRY_DSN_FRONT: ''
      // SENTRY_DSN_FRONT: 'https://abcd1234@sentry.example.com/10'
    })
  },
  list_todos () {
    return mockasync(todos)
  },
  add_todo (newtask) {
    return mockasync({ description: newtask, done: false })
  },
  list_group_messages () {
    return mockasync({
      messages: [
        {
          avatar: 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Mark_Zuckerberg_F8_2018_Keynote_%28cropped_2%29.jpg/1200px-Mark_Zuckerberg_F8_2018_Keynote_%28cropped_2%29.jpg',
          name: 'Markinho',
          message: {text: 'Eai Galera, tranks?', time: '12:34'}
        },
        {
          avatar: 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT12cP23udqvCqHW_2oAvK257g3oVQkv23tOumxtpfFOhHi8a5B',
          name: 'Bill Portões',
          message: {text: 'Fala meu rei', time: '12:35'}
        },
        {
          avatar: 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Mark_Zuckerberg_F8_2018_Keynote_%28cropped_2%29.jpg/1200px-Mark_Zuckerberg_F8_2018_Keynote_%28cropped_2%29.jpg',
          name: 'Markinho',
          message: {text: 'Bora fazer o trabalho?', time: '12:36'}
        },
        {
          avatar: 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT12cP23udqvCqHW_2oAvK257g3oVQkv23tOumxtpfFOhHi8a5B',
          name: 'Bill Portões',
          message: {text: 'Boraaaa', time: '12:37'}
        },
        {
          avatar: 'https://blog.portalpos.com.br/app/uploads/2019/07/steve-jobs-1024x682.png',
          name: 'Steve Trabalhos',
          message: {text: 'Fechou', time: '12:38'}
        },
        {
          avatar: 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQU2JRbbl3LBOm_an3eI5iplFhOoLESyBwUfmWDO49BS1EYuGUE',
          name: 'Doido do foguete',
          message: {text: 'Manda bala', time: '12:39'}
        }
      ]
    })
  },
  list_atendimento_messages () {
    return mockasync({
      messages: [
        {
          avatar: 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Mark_Zuckerberg_F8_2018_Keynote_%28cropped_2%29.jpg/1200px-Mark_Zuckerberg_F8_2018_Keynote_%28cropped_2%29.jpg',
          remetente: 'CLIENTE',
          message: {text: 'Boa Tarde', time: '12:39'}
        },
        {
          avatar: 'https://t3.ftcdn.net/jpg/03/46/83/96/360_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg',
          remetente: 'ATENDENTE',
          message: {text: 'Boa Tarde, no que posso ajudar?', time: '12:39'}
        },
        {
          avatar: 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Mark_Zuckerberg_F8_2018_Keynote_%28cropped_2%29.jpg/1200px-Mark_Zuckerberg_F8_2018_Keynote_%28cropped_2%29.jpg',
          remetente: 'CLIENTE',
          message: {text: 'Estou com fome', time: '12:39'}
        },
        {
          avatar: 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Mark_Zuckerberg_F8_2018_Keynote_%28cropped_2%29.jpg/1200px-Mark_Zuckerberg_F8_2018_Keynote_%28cropped_2%29.jpg',
          remetente: 'CLIENTE',
          message: {text: 'Me vê um lanche', time: '12:39'}
        },
        {
          avatar: 'https://t3.ftcdn.net/jpg/03/46/83/96/360_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg',
          name: 'ATENDENTE',
          message: {text: 'Coca-cola?', time: '12:39'}
        },
        {
          avatar: 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Mark_Zuckerberg_F8_2018_Keynote_%28cropped_2%29.jpg/1200px-Mark_Zuckerberg_F8_2018_Keynote_%28cropped_2%29.jpg',
          name: 'CLIENTE',
          message: {text: 'Hmmmm coquinha gelada', time: '12:39'}
        }
      ]
    })
  },
  change_user_mode (change_to) {
    return mockasync(true)
  },
  encerra_atendimento (atendimento_id) {
    return mockasync(true)
  }
}
