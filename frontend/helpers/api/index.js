import {get, post} from './ajaxutils'

export default {
  login (username, password) {
    return post('/api/login', {username, password})
  },
  logout () {
    return post('/api/logout')
  },
  whoami () {
    return get('/api/whoami')
  },
  settings () {
    return get('/api/settings')
  },
  list_todos () {
    return get('/api/list_todos')
  },
  add_todo (newtask) {
    return post('/api/add_todo', {new_task: newtask})
  },
  list_group_messages () {
    return get('/api/list_group_messages')
  },
  list_atendimento_messages () {
    return get('/api/list_atendimento_messages')
  },
  change_user_mode (change_to) {
    return post('/api/change_user_mode', {change_to})
  },
  encerra_atendimento (atendimento_id) {
    return post('/api/encerra_atendimento', {atendimento_id})
  }
}
