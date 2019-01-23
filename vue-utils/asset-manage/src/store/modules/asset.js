/**
 * 资产页面
 */

import types from '../types.js'

const state = {
    currentFundIndex: 0,
    totalAsset: {
        totalNum: 123456,
        profitAndLossAmount: -300,
        profitAndLossRatio: -20,
        HoldingTime: '1年4.5月'
    },
    holdDetails: [{
            fundId: 1,
            fundCode: 10001,
            fundName: '华夏',
            details: {
                realTimeAmount: 300, //实时金额
                intoWarehouseAmount: 600, //进仓金额
                profitAndLossAmount: -300, //盈亏金额
                profitAndLossRatio: -50, //盈亏比  %
                HoldingTime: 1, //进仓时按权重计算时间  单位月
                monitorIndexs: [{
                        id: 1,
                        name: '指标1'
                    }, {
                        id: 2,
                        name: '指标2'
                    }] //监控指标
            }
        },
        {
            fundId: 2,
            fundCode: 10002,
            fundName: '银河',
            details: {
                realTimeAmount: 300, //实时金额
                intoWarehouseAmount: 600, //进仓金额
                profitAndLossAmount: -300, //盈亏金额
                profitAndLossRatio: -50, //盈亏比  %
                HoldingTime: 1, //进仓时按权重计算时间  单位月
                monitorIndexs: ['指标1', '指标二'] //监控指标
            }
        },
        {
            fundId: 3,
            fundCode: 10003,
            fundName: '华商',
            details: {
                realTimeAmount: 300, //实时金额
                intoWarehouseAmount: 600, //进仓金额
                profitAndLossAmount: -300, //盈亏金额
                profitAndLossRatio: -50, //盈亏比  %
                HoldingTime: 1, //进仓时按权重计算时间  单位月
                monitorIndexs: ['指标1', '指标二'] //监控指标
            }
        }
    ],
    tradeDetails: [{
            date: "2017-8-4",
            fundCode: "10003",
            fundName: "华商",
            realTimeAmount: 456,
            intoWarehouseAmount: 789,
            profitAndLossAmount: 147,
            profitAndLossRatio: 56,
            HoldingTime: 2,
            monitorIndex: '指标1'
        },
        {
            date: "2017-7-4",
            fundCode: "10003",
            fundName: "华商",
            realTimeAmount: 456,
            intoWarehouseAmount: 789,
            profitAndLossAmount: 147,
            profitAndLossRatio: 56,
            HoldingTime: 2,
            monitorIndex: '指标1'
        },
        {
            date: "2017-6-4",
            fundName: "华商",
            fundCode: "10003",
            realTimeAmount: 456,
            intoWarehouseAmount: 789,
            profitAndLossAmount: 147,
            profitAndLossRatio: 56,
            HoldingTime: 2,
            monitorIndex: '指标1'
        }
    ],
    // assetDetailType:'total'
    assetDetailType: 'total',
    tradeSelectVal: '00000',
    followOptions: [{
        label: "复合指标",
        options: [{
                value: 1,
                label: "指标1",
                desc: '111111111111111111111'
            },
            {
                value: 2,
                label: "指标2",
                desc: '2222222222222222'
            },
            {
                value: 3,
                label: "指标3",
                desc: '333333333333333333'
            },
        ]
    }, {
        label: '单一指标',
        options: [{
                value: 4,
                label: "单一指标4",
                desc: '444444444444444'
            },
            {
                value: 5,
                label: "单一指标5",
                desc: '55555555555555'
            }
        ]
    }]
}

var getters = {
    holdDetails(state) {
        return state.holdDetails;
    },
    totalAsset(state) {
        return state.totalAsset;
    },
    filterTradeRecords(state) {
        let filterData = [];
        state.tradeDetails.forEach(item => {
            if (item.fundCode == state.tradeSelectVal) {
                filterData.push(item); //有关计算属性这个值被洗牌，受影响
            }
        })
        return state.tradeSelectVal == '00000' ? state.tradeDetails : filterData;
    },
    currentFundIndex(state) {
        return state.currentFundIndex;
    },
    tradeDetails(state) {
        return state.tradeDetails;
    },
    assetDetailType(state) {
        return state.assetDetailType;
    },
    tradeSelectVal(state) {
        return state.tradeSelectVal;
    },
    followOptions(state) {
        return state.followOptions;
    }
}


const actions = {
    changeCurrentFundIndex({
        commit,
        state
    }, value) {
        commit(types.CHANGE_CURRENT_FUND_INDEX, value);
    },
    changeAssetDetailType({
        commit,
        state
    }, value) {
        commit(types.CHANGE_ASSET_DETAIL_TYPE, value)
    },
    changeFundName({
        commit,
        state
    }, value) {
        commit(types.CHANGE_FUND_NAME, value);
    },
    changeMonitorIndexs({
        commit,
        state
    }, value) {
        commit(types.CHANGE_MONITOR_INDEXS, value)
    }
}

const mutations = {
    [types.CHANGE_CURRENT_FUND_INDEX](state, value) {
        state.currentFundIndex = value;
    },
    [types.CHANGE_ASSET_DETAIL_TYPE](state, value) {
        state.assetDetailType = value;
    },
    [types.CHANGE_FUND_NAME](state, value) {
        state.tradeSelectVal = value;
    },
    [types.CHANGE_MONITOR_INDEXS](state, value) {
        state.holdDetails[state.currentFundIndex].details.monitorIndexs = value;

    }
}


export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}