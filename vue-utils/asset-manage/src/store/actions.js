import types from './types.js'
import { resolve } from 'path';

const actions = {
    incrementAsync({ commit, state }) {
        var p = new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve();
            }, 3000);
        });

        p.then(() => {
            commit(types.INCREMENT);
        }).catch(() => {
            console.log('异步操作')
        });
    }
}

export default actions;