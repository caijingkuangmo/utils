/**
 * 标准设置页面
 */

import types from "../types.js"

/*
 * 建议：清仓指标简单直接  进仓指标可以复杂多个 （保守原则）
 * 
 *  起止计算时间--确认
 * 1） 恒生上涨或下跌到某个点 开始买入或卖出 1000元
 * 2） 恒生上涨或下跌多大幅度（多少个点） 买入或卖出500  需要起止时间
 * 3） 恒生累计下跌5天（同时下跌多少幅度或多少点） 买入  需要起止时间
 *      
 *      基金标的原则（不建议监控基金净值，持仓成本--拆分、折算 会影响分析，建议监控盈亏率  从资金的有效性来看，收益率需兼顾持仓时间）
 * 4） 基金 累计下跌 5% 买入500  需要起止时间
 * 5） 基金 {3月:5%，6月：7%，9月：9%， 12月：12%}  --以进仓时间来(多次进仓 减仓的，基金整体的进仓时间怎么算？)
 *          或 每月1% 每年12% 空档期多少个月   可以合起来，空档期可以在字典里设，不设置字典，设置每月效果
 *          
 *          纯增长率出仓 20% 卖出  不需要时间  rate + isNeed为false
 */

const state = {
    standardDetailType: "composite",
    investmentStandardTypes: ['指数', '基金', '买入', '卖出'],
    panelIndex: [], //选中的指标  单指标
    compositePanelIndex: [], //选中指标  复合指标
    monitorIndexMap: {
        "指数": {
            '10000': '上证',
            '10001': '深指',
            '10002': '创业板',
            '10003': '恒生'
        },
        '基金': {
            '20000': '银河',
            '20001': '华商',
            '20002': '华夏'
        }
    },
    singleStandards: [{
            standardId: 1,
            standardName: "指标一",
            standardDescribe: "牛逼逼Bii毕哔哔哔哔哔哔哔哔哔哔哔哔",
            sendMessage: {
                title: 'bibibbibibibi',
                content: "sadjomvccccccccccccccccccccccccccccldfsjklgkdpfh,oerrrrrrrrrrrrrrrrrrrrrrrrt"
            },
            businessSignals: true,
            investmentStandard: {
                standardType: true,
                standardObject: {
                    code: "10003",
                    name: "恒生"
                },
                indexType: '增长点', //rate  day  day-rate day-spot  1.到达5000点卖出，type为spot+time.isNeed为false  2.上涨50%卖出 type为rate，isNeed为true  3.累计下跌5天 type为day
                rank: {},
                targetValue: 500,
                unit: '点', //% 月 周 天 [天/周/月, %], [天/周/月, 点]
                timeUnit: '月',
                time: {
                    startDate: '2017-8-9'
                }
            }
        },
        {
            standardId: 2,
            standardName: "指标二",
            standardDescribe: "牛逼逼Bii毕哔哔哔哔哔哔哔哔哔哔哔哔",
            sendMessage: {
                title: 'bibibbibibibi',
                content: "sffffffffffffffff461s6g5v2ccccccccc56sd49g615cv5d66666666"
            },
            businessSignals: false,
            investmentStandard: {
                standardType: false,
                standardObject: {
                    code: "20002",
                    name: "华夏"
                },
                indexType: '阶级持仓增长率', //rate  day  day-rate day-spot   1.到达5000点卖出，type为spot+time.isNeed为false  2.上涨50%卖出 type为rate，isNeed为true  3.累计下跌5天 type为day
                rank: {
                    rankMap: [{
                            id: 1,
                            tm: "3",
                            val: "5"
                        },
                        {
                            id: 2,
                            tm: "6",
                            val: "7"
                        },
                        {
                            id: 3,
                            tm: "9",
                            val: "9"
                        },
                        {
                            id: 4,
                            tm: "12",
                            val: "12"
                        }

                    ],
                    every: 2 //固定点数不管这个
                },
                targetValue: 500,
                unit: '%', //% 月 周 天 [天/周/月, %], [天/周/月, 点]
                timeUnit: '天',
                time: {
                    startDate: '2017-8-9'
                }
            }
        },
        {
            standardId: 3,
            standardName: "指标三",
            standardDescribe: "牛逼逼Bii毕哔哔哔哔哔哔哔哔哔哔哔哔",
            sendMessage: {
                title: 'bibibbibibibi',
                content: ""
            },
            businessSignals: true,
            investmentStandard: {
                standardType: false,
                standardObject: {
                    code: "20002",
                    name: "华夏"
                },
                indexType: '持仓增长率', //rate  day  day-rate day-spot   1.到达5000点卖出，type为spot+time.isNeed为false  2.上涨50%卖出 type为rate，isNeed为true  3.累计下跌5天 type为day
                rank: 20,
                targetValue: 500,
                unit: '%', //% 月 周 天 [天/周/月, %], [天/周/月, 点]
                timeUnit: '周',
                time: {
                    startDate: '2017-8-9'
                }
            }
        },
    ],
    compositeStandards: [{
            standardId: 1,
            standardName: "指标一",
            standardDescribe: "121212121212121212121212121",
            sendMessage: {
                title: 'bibibbibibibi',
                content: "25828282825825882588258825882585258"
            },
            businessSignals: true,
            standardType: false,
            standardObject: {
                code: "20002",
                name: "华夏"
            },
            logicalRelation: {
                relation: true,
                indexs: [1, 2]
            }
        },
        {
            standardId: 2,
            standardName: "指标二",
            standardDescribe: "121212121212121212121212121",
            sendMessage: {
                title: 'bibibbibibibi',
                content: "25828282825825882588258825882585258"
            },
            businessSignals: true,
            standardType: false,
            standardObject: {
                code: "20002",
                name: "华夏"
            },
            logicalRelation: {
                relation: false,
                indexs: [3, 4]
            }
        }
    ]
}

var getters = {
    standardDetailType(state) {
        return state.standardDetailType;
    },
    investmentStandardTypes(state) {
        return state.investmentStandardTypes;
    },
    panelIndex(state) {
        return state.panelIndex;
    },
    compositePanelIndex(state) {
        return state.compositePanelIndex;
    },
    singleStandards(state) {
        return state.singleStandards;
    },
    compositeStandards(state) {
        return state.compositeStandards
    },
    filterStandards(state) {
        let filterList = [];
        state.singleStandards.forEach(item => {
            if (item.businessSignals) {
                var businessSignals = "买入";
            } else {
                var businessSignals = "卖出";
            }
            if (item.investmentStandard.standardType) {
                var standardType = "指数";
            } else {
                var standardType = "基金";
            }
            if (state.investmentStandardTypes.includes(businessSignals) || state.investmentStandardTypes.includes(standardType)) {
                filterList.push(item)
            }
        });
        return filterList;
    },
    filterCompositeStandards(state) {
        let filterCompositeList = [];
        state.compositeStandards.forEach(item => {
            if (item.businessSignals) {
                var businessSignals = "买入";
            } else {
                var businessSignals = "卖出";
            }
            if (item.standardType) {
                var standardType = "指数";
            } else {
                var standardType = "基金";
            }
            if (state.investmentStandardTypes.includes(businessSignals) || state.investmentStandardTypes.includes(standardType)) {
                filterCompositeList.push(item)
            }
        });
        return filterCompositeList;
    },
    monitorIndexMap(state) {
        return state.monitorIndexMap;
    }
}

const actions = {
    changeStandardDetailType({
        commit,
        state
    }, value) {
        commit(types.CHANGE_STANDARD_DETAIL_TYPE, value);
    },
    changeInvestmentStandardTypes({
        commit,
        state
    }, value) {
        commit(types.CHANGE_INVESTMENT_STANDARD_TYPES, value);
    },
    changePanelIndex({
        commit,
        state
    }, value) {
        commit(types.CHANGE_PANEL_INDEX, value);
    },
    changeCompositePanelIndex({
        commit,
        state
    }, value) {
        commit(types.CHANGE_COMPOSITE_PANEL_INDEX, value)
    },
    changeStandards({
        commit,
        state
    }, value) {
        commit(types.CHANGE_STANDARDS, value);
    }
}

const mutations = {
    [types.CHANGE_STANDARD_DETAIL_TYPE](state, value) {
        state.standardDetailType = value;
    },
    [types.CHANGE_INVESTMENT_STANDARD_TYPES](state, value) {
        state.investmentStandardTypes = value;
    },
    [types.CHANGE_PANEL_INDEX](state, value) {
        state.panelIndex = value;
    },
    [types.CHANGE_STANDARDS](state, value) {
        state.standards = value;
    },
    [types.CHANGE_COMPOSITE_PANEL_INDEX](state, value) {
        state.compositePanelIndex = value;
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}