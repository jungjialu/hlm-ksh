
// 将后端返回的数据处理成echarts需要的数据格式
function handleEchartData(rowRes) {


        const res = rowRes.map(item => {
            return {
                source: item["n.name"],
                target: item["m.name"],
                rela: item["r.relation"]
            }
        })
        console.log(res, "1")

        const data = [{name: res[0].source, itemStyle: {
            color: '#' + Math.ceil(Math.random() * 1000 % 10) + Math.floor(Math.random() * 1000 % 10) + Math.floor(Math.random() * 1000 % 10)
        }}];
        res.forEach(item => data.push({name: item.target, itemStyle: {
            color: '#' + Math.ceil(Math.random() * 1000 % 10) + Math.floor(Math.random() * 1000 % 10) + Math.floor(Math.random() * 1000 % 10)
        }}))
        const links = res.map(item => {
            return {
                source: item.source,
                target: item.target,
                label: {
                    formatter: item.rela,
                    ...labelStyle
                },
                lineStyle: lineStyle
            }
        })
       return {
            data: data,
            links: links
       }
}

async function handleEvent(oInp, labelStyle, lineStyle) {
    const rowRes = await getData(oInp.value);
    const op = handleEchartData(rowRes);
    renderChart(op.data, op.links)
}


// Search的点击事件
const oSearchBtn = document.getElementsByClassName('btn')[0];
const oInp = document.getElementsByClassName('search')[0];
oSearchBtn.addEventListener('click', function (e) {
    handleEvent(oInp, labelStyle, lineStyle)
})


// 图自适应
window.onresize = function () {
    iChart.resize();
}

// 监听回车
document.onkeydown = function (e) {
    let event = e || window.event;
    if (event.keyCode == 13 && oInp == document.activeElement) handleEvent(oInp, labelStyle, lineStyle);
}

// 监听双击
iChart.on("dblclick", function (e) {
    console.log(e.name)
    oInp.value = e.name
    handleEvent(oInp, labelStyle, lineStyle)
})





