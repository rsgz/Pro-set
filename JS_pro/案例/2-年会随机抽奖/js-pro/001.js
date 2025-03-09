const personArr = ['荒天帝', '萧炎', '林动', '牧尘', '美杜莎']
const mingdan_arr = document.querySelector("div.nei")
const random = () => { return Math.floor(Math.random() * personArr.length) }

function suiji_ele(id) {
    const ele = document.querySelector(id)
    n = random()
    ele.innerText = personArr[n]
    personArr.splice(personArr[n], 1)
}
suiji_ele("#n1")
suiji_ele("#n2")
suiji_ele("#n3")