// 获取数据
async function getData (name) {
    const resp = await fetch('/search_name?name=' + name, {
        method: 'GET',
    })
    const res = await resp.json()
    return res;
}