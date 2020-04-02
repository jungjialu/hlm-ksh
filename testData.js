let data = [
    {name: '林黛玉',},
    {name: 'Lin Daiyu'},
    {name: '颦颦，颦儿，潇湘妃子，林姑娘，林妹妹'},
    {name: '农历二月十二日（花朝节）'},
    {name: '进贾府时10岁，逝世时17岁'},
    {name: '女'},
    {name: '金陵十二钗正册并列第一'},
    {name: '潇湘馆'},
    {name: '绛珠仙草（绛珠仙子）'},
    {name: '苏州'},
    {name: '芙蓉花'},
    {name: '葬花吟、秋窗风雨夕、桃花行'},
];


let mapData = data.map((item) => {
    return {
        ...item,
        itemStyle: {
            color: '#' + Math.ceil(Math.random() * 1000 % 10) + Math.floor(Math.random() * 1000 % 10) + Math.floor(Math.random() * 1000 % 10)
        }
    }
})

let lineStyle = {
    
}
let labelStyle = {
    show: true,
    fontSize: 12,
}
let links = [
    {source: '林黛玉', target: 'Lin Daiyu', label: {formatter: '外文名', ...labelStyle}, lineStyle: lineStyle},
    {source: '林黛玉', target: '颦颦，颦儿，潇湘妃子，林姑娘，林妹妹', label: {formatter: '其他名称', ...labelStyle}, lineStyle: lineStyle},
    {source: '林黛玉', target: '农历二月十二日（花朝节）', label: {formatter: '生    日', ...labelStyle}, lineStyle: lineStyle},
    {source: '林黛玉', target: '进贾府时10岁，逝世时17岁', label: {formatter: '年    龄', ...labelStyle}, lineStyle: lineStyle},
    {source: '林黛玉', target: '女', label: {formatter: '性别', ...labelStyle}, lineStyle: lineStyle},
    {source: '林黛玉', target: '金陵十二钗正册并列第一', label: {formatter: '排    名', ...labelStyle}, lineStyle: lineStyle},
    {source: '林黛玉', target: '潇湘馆', label: {formatter: '大观园居所', ...labelStyle}, lineStyle: lineStyle},
    {source: '林黛玉', target: '绛珠仙草（绛珠仙子）', label: {formatter: '前    世', ...labelStyle}, lineStyle: lineStyle},
    {source: '林黛玉', target: '苏州', label: {formatter: '出生地', ...labelStyle}, lineStyle: lineStyle},
    {source: '林黛玉', target: '芙蓉花', label: {formatter: '花名签', ...labelStyle}, lineStyle: lineStyle},
    {source: '林黛玉', target: '葬花吟、秋窗风雨夕、桃花行', label: {formatter: '代表作品', ...labelStyle}, lineStyle: lineStyle},
]