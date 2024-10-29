const c = Math.PI, x = 2 * c, u = 1e-6, m = x - u;
function E(e) {
  this._ += e[0];
  for (let t = 1, h = e.length; t < h; ++t)
    this._ += arguments[t] + e[t];
}
function A(e) {
  let t = Math.floor(e);
  if (!(t >= 0))
    throw new Error(`invalid digits: ${e}`);
  if (t > 15)
    return E;
  const h = 10 ** t;
  return function(i) {
    this._ += i[0];
    for (let s = 1, n = i.length; s < n; ++s)
      this._ += Math.round(arguments[s] * h) / h + i[s];
  };
}
class L {
  constructor(t) {
    this._x0 = this._y0 = // start of current subpath
    this._x1 = this._y1 = null, this._ = "", this._append = t == null ? E : A(t);
  }
  moveTo(t, h) {
    this._append`M${this._x0 = this._x1 = +t},${this._y0 = this._y1 = +h}`;
  }
  closePath() {
    this._x1 !== null && (this._x1 = this._x0, this._y1 = this._y0, this._append`Z`);
  }
  lineTo(t, h) {
    this._append`L${this._x1 = +t},${this._y1 = +h}`;
  }
  quadraticCurveTo(t, h, i, s) {
    this._append`Q${+t},${+h},${this._x1 = +i},${this._y1 = +s}`;
  }
  bezierCurveTo(t, h, i, s, n, $) {
    this._append`C${+t},${+h},${+i},${+s},${this._x1 = +n},${this._y1 = +$}`;
  }
  arcTo(t, h, i, s, n) {
    if (t = +t, h = +h, i = +i, s = +s, n = +n, n < 0)
      throw new Error(`negative radius: ${n}`);
    let $ = this._x1, r = this._y1, p = i - t, l = s - h, _ = $ - t, o = r - h, a = _ * _ + o * o;
    if (this._x1 === null)
      this._append`M${this._x1 = t},${this._y1 = h}`;
    else if (a > u)
      if (!(Math.abs(o * p - l * _) > u) || !n)
        this._append`L${this._x1 = t},${this._y1 = h}`;
      else {
        let d = i - $, f = s - r, y = p * p + l * l, T = d * d + f * f, g = Math.sqrt(y), v = Math.sqrt(a), w = n * Math.tan((c - Math.acos((y + a - T) / (2 * g * v))) / 2), M = w / v, b = w / g;
        Math.abs(M - 1) > u && this._append`L${t + M * _},${h + M * o}`, this._append`A${n},${n},0,0,${+(o * d > _ * f)},${this._x1 = t + b * p},${this._y1 = h + b * l}`;
      }
  }
  arc(t, h, i, s, n, $) {
    if (t = +t, h = +h, i = +i, $ = !!$, i < 0)
      throw new Error(`negative radius: ${i}`);
    let r = i * Math.cos(s), p = i * Math.sin(s), l = t + r, _ = h + p, o = 1 ^ $, a = $ ? s - n : n - s;
    this._x1 === null ? this._append`M${l},${_}` : (Math.abs(this._x1 - l) > u || Math.abs(this._y1 - _) > u) && this._append`L${l},${_}`, i && (a < 0 && (a = a % x + x), a > m ? this._append`A${i},${i},0,1,${o},${t - r},${h - p}A${i},${i},0,1,${o},${this._x1 = l},${this._y1 = _}` : a > u && this._append`A${i},${i},0,${+(a >= c)},${o},${this._x1 = t + i * Math.cos(n)},${this._y1 = h + i * Math.sin(n)}`);
  }
  rect(t, h, i, s) {
    this._append`M${this._x0 = this._x1 = +t},${this._y0 = this._y1 = +h}h${i = +i}v${+s}h${-i}Z`;
  }
  toString() {
    return this._;
  }
}
function P(e) {
  return function() {
    return e;
  };
}
function q(e) {
  let t = 3;
  return e.digits = function(h) {
    if (!arguments.length)
      return t;
    if (h == null)
      t = null;
    else {
      const i = Math.floor(h);
      if (!(i >= 0))
        throw new RangeError(`invalid digits: ${h}`);
      t = i;
    }
    return e;
  }, () => new L(t);
}
export {
  P as c,
  q as w
};
