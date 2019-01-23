/**
 * 指数跟踪页面
 *  指数：  名称，代号，多少点，时间  涨跌幅   最近一周，最近一月，最近一年   累计涨跌幅  最大连涨天数 最大连跌天数 最低点(时间)  最高点（时间）  后面可加极端涨跌幅天（比如3% 5%）
 *  基金：  名称，代号，基金净值，时间 涨跌幅  最近一周，最近一月，最近一年   累计涨跌幅
 */

import types from '../types.js'

const state = {
    stocks: {
        "zhishu": [{
                id: 1,
                code: "10000",
                name: "创业板指数",
                number: 8000,
                date: '2018-8-9',
                rate: '1%',
                lately: {
                    '最近一周': {
                        rate: '2%',
                        maxRiseDays: 4,
                        maxDropDays: 2,
                        maxSpot: {
                            num: 8100,
                            date: "2018-5-6"
                        },
                        minSpot: {
                            num: 6200,
                            date: "2018-5-6"
                        }
                    },
                    "最近一月": {
                        rate: '3%',
                        maxRiseDays: 4,
                        maxDropDays: 2,
                        maxSpot: {
                            num: 8100,
                            date: "2018-5-6"
                        },
                        minSpot: {
                            num: 6200,
                            date: "2018-5-6"
                        }
                    },
                    "最近一年": {
                        rate: '4%',
                        maxRiseDays: 4,
                        maxDropDays: 2,
                        maxSpot: {
                            num: 8100,
                            date: "2018-5-6"
                        },
                        minSpot: {
                            num: 6200,
                            date: "2018-5-6"
                        }
                    }
                }
            },
            {
                id: 2,
                code: "10001",
                name: "上证指数",
                number: 9000,
                date: '2018-8-9',
                rate: '1%',
                lately: {
                    '最近一周': {
                        rate: '2%',
                        maxRiseDays: 4,
                        maxDropDays: 2,
                        maxSpot: {
                            num: 8100,
                            date: "2018-5-6"
                        },
                        minSpot: {
                            num: 6200,
                            date: "2018-5-6"
                        }
                    },
                    "最近一月": {
                        rate: '2%',
                        maxRiseDays: 4,
                        maxDropDays: 2,
                        maxSpot: {
                            num: 8100,
                            date: "2018-5-6"
                        },
                        minSpot: {
                            num: 6200,
                            date: "2018-5-6"
                        }
                    },
                    "最近一年": {
                        rate: '2%',
                        maxRiseDays: 4,
                        maxDropDays: 2,
                        maxSpot: {
                            num: 8100,
                            date: "2018-5-6"
                        },
                        minSpot: {
                            num: 6200,
                            date: "2018-5-6"
                        }
                    }
                }
            },
        ],
        "jijin": [{
            id: 3,
            code: "10002",
            name: "华夏",
            number: 2.3,
            date: '2018-8-9',
            rate: '1%',
            lately: {
                '最近一周': {
                    rate: '2%',
                },
                "最近一月": {
                    rate: '2%',
                },
                "最近一年": {
                    rate: '2%',
                }
            }
        }]
    }
}

var getters = {
    stocks(state) {
        return state.stocks;
    },
    selectOptions(state) {
        let options = [];
        Object.keys(state.stocks).forEach(indexVal => {
            var indexItem = state.stocks[indexVal];
            var option = {
                value: indexVal,
                label: indexVal == 'zhishu' ? '指数' : '基金',
                children: []
            };
            indexItem.forEach(item => {
                option.children.push({
                    value: item.id,
                    label: item.name
                })
            });
            options.push(option);
        });
        return options;
    }
}

const actions = {
    [types.CHANGE_STOCKS]({
        commit,
        state
    }, value) {
        commit(types.CHANGE_STOCKS, value);
    },
    [types.DEL_STOCK]({
        commit,
        state
    }, value) {
        commit(types.DEL_STOCK, value);
    }
}

const mutations = {
    [types.CHANGE_STOCKS](state, value) {
        if (value.type) {
            state.stocks['zhishu'].push({
                id: 6,
                code: value.number,
                name: "恒生指数",
                number: 9000,
                date: '2018-8-9',
                rate: '1%',
                lately: {
                    '最近一周': {
                        rate: '2%',
                        maxRiseDays: 4,
                        maxDropDays: 2,
                        maxSpot: {
                            num: 8100,
                            date: "2018-5-6"
                        },
                        minSpot: {
                            num: 6200,
                            date: "2018-5-6"
                        }
                    },
                    "最近一月": {
                        rate: '2%',
                        maxRiseDays: 4,
                        maxDropDays: 2,
                        maxSpot: {
                            num: 8100,
                            date: "2018-5-6"
                        },
                        minSpot: {
                            num: 6200,
                            date: "2018-5-6"
                        }
                    },
                    "最近一年": {
                        rate: '2%',
                        maxRiseDays: 4,
                        maxDropDays: 2,
                        maxSpot: {
                            num: 8100,
                            date: "2018-5-6"
                        },
                        minSpot: {
                            num: 6200,
                            date: "2018-5-6"
                        }
                    }
                }
            })
        } else {
            state.stocks['jijin'].push({
                id: 7,
                code: value.number,
                name: "银河",
                number: 9000,
                date: '2018-8-9',
                rate: '1%',
                lately: {
                    '最近一周': {
                        rate: '2%',
                    },
                    "最近一月": {
                        rate: '2%',
                    },
                    "最近一年": {
                        rate: '2%',
                    }
                }
            })
        }
    },
    [types.DEL_STOCK](state, value) {
        state.stocks[value.indexType].splice(value.index, 1);
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}