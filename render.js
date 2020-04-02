function renderChart (data, links) {
    console.log(data, links, "2");
    let option = {
        title: {
            text: ' '
        },
        tooltip: {},
        animationDurationUpdate: 1500,
        animationEasingUpdate: 'quinticInOut',
        series: [
            {
                type: 'graph',
                layout: 'force',
                force: {
                        repulsion: [1000,2000],
                        gravity: 0.3,
                        layoutAnimation: true,
                        edgeLength: 65
                },
                draggable: true,
                symbolSize: 50,
                roam: 'scale',
                label: {
                    show: true
                },
                edgeSymbol: ['circle', 'arrow'],
                edgeSymbolSize: [4, 5],
                edgeLabel: {
                    fontSize: 20
                },
                data: data,
                // links: [],
                links: links,
                lineStyle: {
                    opacity: 0.9,
                    width: 2,
                    curveness: 0
                }
            }
        ]
    };
        iChart.setOption(option);
}