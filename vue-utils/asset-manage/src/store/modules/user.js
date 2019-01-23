/**
 * 用户模块
 */

import types from '../types.js'

const state = {

}

var getters = {

}

const actions = {
    increment({
        commit,
        state
    }) {
        commit(types.INCREMENT);
    }
}

const mutations = {
    [types.INCREMENT](state) {
        state.count++;
    }
}


export default {
    state,
    getters,
    actions,
    mutations
}