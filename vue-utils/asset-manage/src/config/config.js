//standard
const fundIndexTypes = {
    '持仓增长率': {
        type: 'rate',
        needStartTime: false,
        needTimeUnit: false,
        edit: {
            isTable: false
        },
        unit: '%'
    }, //持仓时间算法
    '指定时间增长率': {
        type: 'rate',
        needStartTime: true,
        needTimeUnit: false,
        edit: {
            isTable: false
        },
        unit: '%'
    }, //找到这天的盈亏率，以此为基准
    '阶级持仓增长率': {
        type: 'day-rate',
        needStartTime: false,
        needTimeUnit: true,
        edit: {
            isTable: true,
            hasEvery: true
        },
        unit: '%'
    }
}

const StockMarketIndexTypes = {
    '固定点': {
        type: 'spot',
        needStartTime: false,
        needTimeUnit: false,
        edit: {
            isTable: false
        },
        unit: '点'
    },
    '增长点': {
        type: 'spot',
        needStartTime: true,
        needTimeUnit: false,
        edit: {
            isTable: false
        },
        unit: '点'
    },
    '增长率': {
        type: 'rate',
        needStartTime: true,
        needTimeUnit: false,
        edit: {
            isTable: false
        },
        unit: '%'
    },
    '累计天数': {
        type: 'day',
        needStartTime: false,
        needTimeUnit: true,
        edit: {
            isTable: false
        },
        unit: ''
    },
    '阶级固定点': {
        type: 'day-spot',
        needStartTime: false,
        needTimeUnit: true,
        edit: {
            isTable: true,
            hasEvery: false
        },
        unit: '点'
    }, //按持仓时间来
    '阶级增长点': {
        type: 'day-spot',
        needStartTime: true,
        needTimeUnit: true,
        edit: {
            isTable: true,
            hasEvery: true
        },
        unit: '点'
    }
}

export default {
    fundIndexTypes,
    StockMarketIndexTypes
}