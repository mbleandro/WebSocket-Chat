import api from '~api'

export const state = () => ({
  currentUser: undefined,
  user_type: 'CLIENTE',
  chat: 'GRUPO',
  user: null
})

export const mutations = {
  setCurrentUser (state, user) {
    state.user = user
  },
  SET_USER_CLIENTE (state) {
    state.user_type = 'CLIENTE'
  },
  SET_USER_ATENDENTE (state) {
    state.user_type = 'ATENDENTE'
  },
  SET_CHAT_GRUPO (state) {
    state.chat = 'GRUPO'
  },
  SET_CHAT_ATENDIMENTO (state) {
    state.chat = 'ATENDIMENTO'
  }
}

export const getters = {
  loggedIn (state) {
    return !!(state.currentUser && state.currentUser.permissions)
  },
  user_type (state) {
    return state.user_type
  },
  chat (state) {
    return state.chat
  },
  user (state) {
    return state.user
  }
}

export const actions = {
  async whoami ({ commit }) {
    const data = await api.whoami()
    if (data.authenticated) {
      commit('setCurrentUser', data.user)
    } else {
      commit('setCurrentUser', null)
    }
  }
}
