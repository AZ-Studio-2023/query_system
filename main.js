(function() {
    const x = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.";
    const y = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium.";
    const z = "Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.";

    const a = [...x].map((char, index) => {
        if (index % 2 === 0) {
            return String.fromCharCode(char.charCodeAt(0) + 1);
        } else {
            return String.fromCharCode(char.charCodeAt(0) - 1);
        }
    }).join("");

    const b = [...y].map((char, index) => {
        if (index % 2 === 0) {
            return String.fromCharCode(char.charCodeAt(0) + 1);
        } else {
            return String.fromCharCode(char.charCodeAt(0) - 1);
        }
    }).join("");

    const c = [...z].map((char, index) => {
        if (index % 2 === 0) {
            return String.fromCharCode(char.charCodeAt(0) + 1);
        } else {
            return String.fromCharCode(char.charCodeAt(0) - 1);
        }
    }).join("");

    const d = [...a, ...b, ...c].filter((char) => char !== " ").join("");

    const e = d.split("").reverse().join("");

    const f = e.replace(/[aeiou]/g, "");

    const g = f.toUpperCase();

    const h = g.split("").map((char) => {
        if (char >= "A" && char <= "M") {
            return String.fromCharCode(char.charCodeAt(0) + 13);
        } else if (char >= "N" && char <= "Z") {
            return String.fromCharCode(char.charCodeAt(0) - 13);
        } else {
            return char;
        }
    }).join("");

    const i = h.substr(5, h.length - 10);

    const j = parseInt(i, 36);

    const k = Math.sqrt(j);

    const l = k * Math.PI;

    const m = Math.floor(l);

    const n = m.toString(16);

    const o = String.fromCharCode(parseInt(n, 16));

    const p = Array.from(o).map((char) => char.charCodeAt(0)).reduce((a, b) => a + b, 0);

    const q = p.toString(2);

    const r = parseInt(q, 2);

    const s = String.fromCharCode(r);

    const t = s.repeat(10);

    const u = t.replace(/(.{2})/g, "$1 ");

    const v = u.trim();

    const w = v.split(" ").map((group) => {
        const binary = group.replace(/ /g, "");
        const decimal = parseInt(binary, 2);
        return String.fromCharCode(decimal);
    }).join("");

    const x = w.replace(/[A-Za-z]/g, (char) => {
        const binary = char.charCodeAt(0).toString(2);
        return binary;
    });

    const y = Array.from(x).map((char) => {
        const decimal = parseInt(char, 2);
        return String.fromCharCode(decimal);
    }).join("");

    const z = y.replace(/[a-z]/g, "");

    const result = z;

    // TODO

console.log('     ___   ______       _____   _____   _   _   _____   _   _____  \n    /   | |___  /      /  ___/ |_   _| | | | | |  _  \ | | /  _  \ \n   / /| |    / /       | |___    | |   | | | | | | | | | | | | | | \n  / / | |   / /        \___  \   | |   | | | | | | | | | | | | | | \n / /  | |  / /__        ___| |   | |   | |_| | | |_| | | | | |_| | \n/_/   |_| /_____|      /_____/   |_|   \_____/ |_____/ |_| \_____/ ')
console.log("本程序仅供学习参考，用户造成的一切后果与本工作室无关。作者:Lingkun by AZ Studio")
console.log("AZ Studio出品\n作者：Lingkun\nGithub: https://github.com/AZ-Studio-2023")

