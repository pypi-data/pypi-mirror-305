import { I as Be, J as Ze, R as Xe, K as qe, L as Dn, M as $t, N as Mn, O as ye, P as ke, c as xt, s as _n, g as Sn, B as Un, C as Yn, b as Fn, a as Ln, Q as nt, D as En, e as An, z as In, l as qt, j as Pt, k as Wn, f as On } from "./mermaid-a09fe7cd.js";
import { b as Hn, t as Ue, c as Nn, a as Vn, l as zn } from "./linear-2bc336bd.js";
import { i as Pn } from "./init-f9637058.js";
function Rn(t, e) {
  let n;
  if (e === void 0)
    for (const r of t)
      r != null && (n < r || n === void 0 && r >= r) && (n = r);
  else {
    let r = -1;
    for (let i of t)
      (i = e(i, ++r, t)) != null && (n < i || n === void 0 && i >= i) && (n = i);
  }
  return n;
}
function Bn(t, e) {
  let n;
  if (e === void 0)
    for (const r of t)
      r != null && (n > r || n === void 0 && r >= r) && (n = r);
  else {
    let r = -1;
    for (let i of t)
      (i = e(i, ++r, t)) != null && (n > i || n === void 0 && i >= i) && (n = i);
  }
  return n;
}
function Zn(t) {
  return t;
}
var Bt = 1, te = 2, ue = 3, Rt = 4, Ye = 1e-6;
function Xn(t) {
  return "translate(" + t + ",0)";
}
function qn(t) {
  return "translate(0," + t + ")";
}
function Gn(t) {
  return (e) => +t(e);
}
function jn(t, e) {
  return e = Math.max(0, t.bandwidth() - e * 2) / 2, t.round() && (e = Math.round(e)), (n) => +t(n) + e;
}
function Qn() {
  return !this.__axis;
}
function Ge(t, e) {
  var n = [], r = null, i = null, s = 6, a = 6, y = 3, S = typeof window < "u" && window.devicePixelRatio > 1 ? 0 : 0.5, k = t === Bt || t === Rt ? -1 : 1, C = t === Rt || t === te ? "x" : "y", F = t === Bt || t === ue ? Xn : qn;
  function w(x) {
    var q = r ?? (e.ticks ? e.ticks.apply(e, n) : e.domain()), g = i ?? (e.tickFormat ? e.tickFormat.apply(e, n) : Zn), L = Math.max(s, 0) + y, O = e.range(), W = +O[0] + S, B = +O[O.length - 1] + S, Z = (e.bandwidth ? jn : Gn)(e.copy(), S), Q = x.selection ? x.selection() : x, b = Q.selectAll(".domain").data([null]), A = Q.selectAll(".tick").data(q, e).order(), T = A.exit(), Y = A.enter().append("g").attr("class", "tick"), D = A.select("line"), v = A.select("text");
    b = b.merge(b.enter().insert("path", ".tick").attr("class", "domain").attr("stroke", "currentColor")), A = A.merge(Y), D = D.merge(Y.append("line").attr("stroke", "currentColor").attr(C + "2", k * s)), v = v.merge(Y.append("text").attr("fill", "currentColor").attr(C, k * L).attr("dy", t === Bt ? "0em" : t === ue ? "0.71em" : "0.32em")), x !== Q && (b = b.transition(x), A = A.transition(x), D = D.transition(x), v = v.transition(x), T = T.transition(x).attr("opacity", Ye).attr("transform", function(o) {
      return isFinite(o = Z(o)) ? F(o + S) : this.getAttribute("transform");
    }), Y.attr("opacity", Ye).attr("transform", function(o) {
      var d = this.parentNode.__axis;
      return F((d && isFinite(d = d(o)) ? d : Z(o)) + S);
    })), T.remove(), b.attr("d", t === Rt || t === te ? a ? "M" + k * a + "," + W + "H" + S + "V" + B + "H" + k * a : "M" + S + "," + W + "V" + B : a ? "M" + W + "," + k * a + "V" + S + "H" + B + "V" + k * a : "M" + W + "," + S + "H" + B), A.attr("opacity", 1).attr("transform", function(o) {
      return F(Z(o) + S);
    }), D.attr(C + "2", k * s), v.attr(C, k * L).text(g), Q.filter(Qn).attr("fill", "none").attr("font-size", 10).attr("font-family", "sans-serif").attr("text-anchor", t === te ? "start" : t === Rt ? "end" : "middle"), Q.each(function() {
      this.__axis = Z;
    });
  }
  return w.scale = function(x) {
    return arguments.length ? (e = x, w) : e;
  }, w.ticks = function() {
    return n = Array.from(arguments), w;
  }, w.tickArguments = function(x) {
    return arguments.length ? (n = x == null ? [] : Array.from(x), w) : n.slice();
  }, w.tickValues = function(x) {
    return arguments.length ? (r = x == null ? null : Array.from(x), w) : r && r.slice();
  }, w.tickFormat = function(x) {
    return arguments.length ? (i = x, w) : i;
  }, w.tickSize = function(x) {
    return arguments.length ? (s = a = +x, w) : s;
  }, w.tickSizeInner = function(x) {
    return arguments.length ? (s = +x, w) : s;
  }, w.tickSizeOuter = function(x) {
    return arguments.length ? (a = +x, w) : a;
  }, w.tickPadding = function(x) {
    return arguments.length ? (y = +x, w) : y;
  }, w.offset = function(x) {
    return arguments.length ? (S = +x, w) : S;
  }, w;
}
function Jn(t) {
  return Ge(Bt, t);
}
function Kn(t) {
  return Ge(ue, t);
}
const $n = Math.PI / 180, tr = 180 / Math.PI, Gt = 18, je = 0.96422, Qe = 1, Je = 0.82521, Ke = 4 / 29, wt = 6 / 29, $e = 3 * wt * wt, er = wt * wt * wt;
function tn(t) {
  if (t instanceof ot)
    return new ot(t.l, t.a, t.b, t.opacity);
  if (t instanceof ut)
    return en(t);
  t instanceof Xe || (t = Dn(t));
  var e = ie(t.r), n = ie(t.g), r = ie(t.b), i = ee((0.2225045 * e + 0.7168786 * n + 0.0606169 * r) / Qe), s, a;
  return e === n && n === r ? s = a = i : (s = ee((0.4360747 * e + 0.3850649 * n + 0.1430804 * r) / je), a = ee((0.0139322 * e + 0.0971045 * n + 0.7141733 * r) / Je)), new ot(116 * i - 16, 500 * (s - i), 200 * (i - a), t.opacity);
}
function nr(t, e, n, r) {
  return arguments.length === 1 ? tn(t) : new ot(t, e, n, r ?? 1);
}
function ot(t, e, n, r) {
  this.l = +t, this.a = +e, this.b = +n, this.opacity = +r;
}
Be(ot, nr, Ze(qe, {
  brighter(t) {
    return new ot(this.l + Gt * (t ?? 1), this.a, this.b, this.opacity);
  },
  darker(t) {
    return new ot(this.l - Gt * (t ?? 1), this.a, this.b, this.opacity);
  },
  rgb() {
    var t = (this.l + 16) / 116, e = isNaN(this.a) ? t : t + this.a / 500, n = isNaN(this.b) ? t : t - this.b / 200;
    return e = je * ne(e), t = Qe * ne(t), n = Je * ne(n), new Xe(
      re(3.1338561 * e - 1.6168667 * t - 0.4906146 * n),
      re(-0.9787684 * e + 1.9161415 * t + 0.033454 * n),
      re(0.0719453 * e - 0.2289914 * t + 1.4052427 * n),
      this.opacity
    );
  }
}));
function ee(t) {
  return t > er ? Math.pow(t, 1 / 3) : t / $e + Ke;
}
function ne(t) {
  return t > wt ? t * t * t : $e * (t - Ke);
}
function re(t) {
  return 255 * (t <= 31308e-7 ? 12.92 * t : 1.055 * Math.pow(t, 1 / 2.4) - 0.055);
}
function ie(t) {
  return (t /= 255) <= 0.04045 ? t / 12.92 : Math.pow((t + 0.055) / 1.055, 2.4);
}
function rr(t) {
  if (t instanceof ut)
    return new ut(t.h, t.c, t.l, t.opacity);
  if (t instanceof ot || (t = tn(t)), t.a === 0 && t.b === 0)
    return new ut(NaN, 0 < t.l && t.l < 100 ? 0 : NaN, t.l, t.opacity);
  var e = Math.atan2(t.b, t.a) * tr;
  return new ut(e < 0 ? e + 360 : e, Math.sqrt(t.a * t.a + t.b * t.b), t.l, t.opacity);
}
function fe(t, e, n, r) {
  return arguments.length === 1 ? rr(t) : new ut(t, e, n, r ?? 1);
}
function ut(t, e, n, r) {
  this.h = +t, this.c = +e, this.l = +n, this.opacity = +r;
}
function en(t) {
  if (isNaN(t.h))
    return new ot(t.l, 0, 0, t.opacity);
  var e = t.h * $n;
  return new ot(t.l, Math.cos(e) * t.c, Math.sin(e) * t.c, t.opacity);
}
Be(ut, fe, Ze(qe, {
  brighter(t) {
    return new ut(this.h, this.c, this.l + Gt * (t ?? 1), this.opacity);
  },
  darker(t) {
    return new ut(this.h, this.c, this.l - Gt * (t ?? 1), this.opacity);
  },
  rgb() {
    return en(this).rgb();
  }
}));
function ir(t) {
  return function(e, n) {
    var r = t((e = fe(e)).h, (n = fe(n)).h), i = $t(e.c, n.c), s = $t(e.l, n.l), a = $t(e.opacity, n.opacity);
    return function(y) {
      return e.h = r(y), e.c = i(y), e.l = s(y), e.opacity = a(y), e + "";
    };
  };
}
const sr = ir(Mn);
function ar(t, e) {
  t = t.slice();
  var n = 0, r = t.length - 1, i = t[n], s = t[r], a;
  return s < i && (a = n, n = r, r = a, a = i, i = s, s = a), t[n] = e.floor(i), t[r] = e.ceil(s), t;
}
const se = /* @__PURE__ */ new Date(), ae = /* @__PURE__ */ new Date();
function $(t, e, n, r) {
  function i(s) {
    return t(s = arguments.length === 0 ? /* @__PURE__ */ new Date() : /* @__PURE__ */ new Date(+s)), s;
  }
  return i.floor = (s) => (t(s = /* @__PURE__ */ new Date(+s)), s), i.ceil = (s) => (t(s = new Date(s - 1)), e(s, 1), t(s), s), i.round = (s) => {
    const a = i(s), y = i.ceil(s);
    return s - a < y - s ? a : y;
  }, i.offset = (s, a) => (e(s = /* @__PURE__ */ new Date(+s), a == null ? 1 : Math.floor(a)), s), i.range = (s, a, y) => {
    const S = [];
    if (s = i.ceil(s), y = y == null ? 1 : Math.floor(y), !(s < a) || !(y > 0))
      return S;
    let k;
    do
      S.push(k = /* @__PURE__ */ new Date(+s)), e(s, y), t(s);
    while (k < s && s < a);
    return S;
  }, i.filter = (s) => $((a) => {
    if (a >= a)
      for (; t(a), !s(a); )
        a.setTime(a - 1);
  }, (a, y) => {
    if (a >= a)
      if (y < 0)
        for (; ++y <= 0; )
          for (; e(a, -1), !s(a); )
            ;
      else
        for (; --y >= 0; )
          for (; e(a, 1), !s(a); )
            ;
  }), n && (i.count = (s, a) => (se.setTime(+s), ae.setTime(+a), t(se), t(ae), Math.floor(n(se, ae))), i.every = (s) => (s = Math.floor(s), !isFinite(s) || !(s > 0) ? null : s > 1 ? i.filter(r ? (a) => r(a) % s === 0 : (a) => i.count(0, a) % s === 0) : i)), i;
}
const Dt = $(() => {
}, (t, e) => {
  t.setTime(+t + e);
}, (t, e) => e - t);
Dt.every = (t) => (t = Math.floor(t), !isFinite(t) || !(t > 0) ? null : t > 1 ? $((e) => {
  e.setTime(Math.floor(e / t) * t);
}, (e, n) => {
  e.setTime(+e + n * t);
}, (e, n) => (n - e) / t) : Dt);
Dt.range;
const ft = 1e3, rt = ft * 60, ht = rt * 60, dt = ht * 24, pe = dt * 7, Fe = dt * 30, oe = dt * 365, gt = $((t) => {
  t.setTime(t - t.getMilliseconds());
}, (t, e) => {
  t.setTime(+t + e * ft);
}, (t, e) => (e - t) / ft, (t) => t.getUTCSeconds());
gt.range;
const Et = $((t) => {
  t.setTime(t - t.getMilliseconds() - t.getSeconds() * ft);
}, (t, e) => {
  t.setTime(+t + e * rt);
}, (t, e) => (e - t) / rt, (t) => t.getMinutes());
Et.range;
const or = $((t) => {
  t.setUTCSeconds(0, 0);
}, (t, e) => {
  t.setTime(+t + e * rt);
}, (t, e) => (e - t) / rt, (t) => t.getUTCMinutes());
or.range;
const At = $((t) => {
  t.setTime(t - t.getMilliseconds() - t.getSeconds() * ft - t.getMinutes() * rt);
}, (t, e) => {
  t.setTime(+t + e * ht);
}, (t, e) => (e - t) / ht, (t) => t.getHours());
At.range;
const cr = $((t) => {
  t.setUTCMinutes(0, 0, 0);
}, (t, e) => {
  t.setTime(+t + e * ht);
}, (t, e) => (e - t) / ht, (t) => t.getUTCHours());
cr.range;
const yt = $(
  (t) => t.setHours(0, 0, 0, 0),
  (t, e) => t.setDate(t.getDate() + e),
  (t, e) => (e - t - (e.getTimezoneOffset() - t.getTimezoneOffset()) * rt) / dt,
  (t) => t.getDate() - 1
);
yt.range;
const Te = $((t) => {
  t.setUTCHours(0, 0, 0, 0);
}, (t, e) => {
  t.setUTCDate(t.getUTCDate() + e);
}, (t, e) => (e - t) / dt, (t) => t.getUTCDate() - 1);
Te.range;
const lr = $((t) => {
  t.setUTCHours(0, 0, 0, 0);
}, (t, e) => {
  t.setUTCDate(t.getUTCDate() + e);
}, (t, e) => (e - t) / dt, (t) => Math.floor(t / dt));
lr.range;
function Tt(t) {
  return $((e) => {
    e.setDate(e.getDate() - (e.getDay() + 7 - t) % 7), e.setHours(0, 0, 0, 0);
  }, (e, n) => {
    e.setDate(e.getDate() + n * 7);
  }, (e, n) => (n - e - (n.getTimezoneOffset() - e.getTimezoneOffset()) * rt) / pe);
}
const Ot = Tt(0), It = Tt(1), nn = Tt(2), rn = Tt(3), kt = Tt(4), sn = Tt(5), an = Tt(6);
Ot.range;
It.range;
nn.range;
rn.range;
kt.range;
sn.range;
an.range;
function bt(t) {
  return $((e) => {
    e.setUTCDate(e.getUTCDate() - (e.getUTCDay() + 7 - t) % 7), e.setUTCHours(0, 0, 0, 0);
  }, (e, n) => {
    e.setUTCDate(e.getUTCDate() + n * 7);
  }, (e, n) => (n - e) / pe);
}
const on = bt(0), jt = bt(1), ur = bt(2), fr = bt(3), Mt = bt(4), hr = bt(5), dr = bt(6);
on.range;
jt.range;
ur.range;
fr.range;
Mt.range;
hr.range;
dr.range;
const Wt = $((t) => {
  t.setDate(1), t.setHours(0, 0, 0, 0);
}, (t, e) => {
  t.setMonth(t.getMonth() + e);
}, (t, e) => e.getMonth() - t.getMonth() + (e.getFullYear() - t.getFullYear()) * 12, (t) => t.getMonth());
Wt.range;
const mr = $((t) => {
  t.setUTCDate(1), t.setUTCHours(0, 0, 0, 0);
}, (t, e) => {
  t.setUTCMonth(t.getUTCMonth() + e);
}, (t, e) => e.getUTCMonth() - t.getUTCMonth() + (e.getUTCFullYear() - t.getUTCFullYear()) * 12, (t) => t.getUTCMonth());
mr.range;
const mt = $((t) => {
  t.setMonth(0, 1), t.setHours(0, 0, 0, 0);
}, (t, e) => {
  t.setFullYear(t.getFullYear() + e);
}, (t, e) => e.getFullYear() - t.getFullYear(), (t) => t.getFullYear());
mt.every = (t) => !isFinite(t = Math.floor(t)) || !(t > 0) ? null : $((e) => {
  e.setFullYear(Math.floor(e.getFullYear() / t) * t), e.setMonth(0, 1), e.setHours(0, 0, 0, 0);
}, (e, n) => {
  e.setFullYear(e.getFullYear() + n * t);
});
mt.range;
const pt = $((t) => {
  t.setUTCMonth(0, 1), t.setUTCHours(0, 0, 0, 0);
}, (t, e) => {
  t.setUTCFullYear(t.getUTCFullYear() + e);
}, (t, e) => e.getUTCFullYear() - t.getUTCFullYear(), (t) => t.getUTCFullYear());
pt.every = (t) => !isFinite(t = Math.floor(t)) || !(t > 0) ? null : $((e) => {
  e.setUTCFullYear(Math.floor(e.getUTCFullYear() / t) * t), e.setUTCMonth(0, 1), e.setUTCHours(0, 0, 0, 0);
}, (e, n) => {
  e.setUTCFullYear(e.getUTCFullYear() + n * t);
});
pt.range;
function gr(t, e, n, r, i, s) {
  const a = [
    [gt, 1, ft],
    [gt, 5, 5 * ft],
    [gt, 15, 15 * ft],
    [gt, 30, 30 * ft],
    [s, 1, rt],
    [s, 5, 5 * rt],
    [s, 15, 15 * rt],
    [s, 30, 30 * rt],
    [i, 1, ht],
    [i, 3, 3 * ht],
    [i, 6, 6 * ht],
    [i, 12, 12 * ht],
    [r, 1, dt],
    [r, 2, 2 * dt],
    [n, 1, pe],
    [e, 1, Fe],
    [e, 3, 3 * Fe],
    [t, 1, oe]
  ];
  function y(k, C, F) {
    const w = C < k;
    w && ([k, C] = [C, k]);
    const x = F && typeof F.range == "function" ? F : S(k, C, F), q = x ? x.range(k, +C + 1) : [];
    return w ? q.reverse() : q;
  }
  function S(k, C, F) {
    const w = Math.abs(C - k) / F, x = Hn(([, , L]) => L).right(a, w);
    if (x === a.length)
      return t.every(Ue(k / oe, C / oe, F));
    if (x === 0)
      return Dt.every(Math.max(Ue(k, C, F), 1));
    const [q, g] = a[w / a[x - 1][2] < a[x][2] / w ? x - 1 : x];
    return q.every(g);
  }
  return [y, S];
}
const [yr, kr] = gr(mt, Wt, Ot, yt, At, Et);
function ce(t) {
  if (0 <= t.y && t.y < 100) {
    var e = new Date(-1, t.m, t.d, t.H, t.M, t.S, t.L);
    return e.setFullYear(t.y), e;
  }
  return new Date(t.y, t.m, t.d, t.H, t.M, t.S, t.L);
}
function le(t) {
  if (0 <= t.y && t.y < 100) {
    var e = new Date(Date.UTC(-1, t.m, t.d, t.H, t.M, t.S, t.L));
    return e.setUTCFullYear(t.y), e;
  }
  return new Date(Date.UTC(t.y, t.m, t.d, t.H, t.M, t.S, t.L));
}
function Yt(t, e, n) {
  return { y: t, m: e, d: n, H: 0, M: 0, S: 0, L: 0 };
}
function pr(t) {
  var e = t.dateTime, n = t.date, r = t.time, i = t.periods, s = t.days, a = t.shortDays, y = t.months, S = t.shortMonths, k = Ft(i), C = Lt(i), F = Ft(s), w = Lt(s), x = Ft(a), q = Lt(a), g = Ft(y), L = Lt(y), O = Ft(S), W = Lt(S), B = {
    a: c,
    A: X,
    b: f,
    B: h,
    c: null,
    d: Oe,
    e: Oe,
    f: zr,
    g: Jr,
    G: $r,
    H: Hr,
    I: Nr,
    j: Vr,
    L: cn,
    m: Pr,
    M: Rr,
    p: U,
    q: G,
    Q: Ve,
    s: ze,
    S: Br,
    u: Zr,
    U: Xr,
    V: qr,
    w: Gr,
    W: jr,
    x: null,
    X: null,
    y: Qr,
    Y: Kr,
    Z: ti,
    "%": Ne
  }, Z = {
    a: H,
    A: V,
    b: I,
    B: z,
    c: null,
    d: He,
    e: He,
    f: ii,
    g: mi,
    G: yi,
    H: ei,
    I: ni,
    j: ri,
    L: un,
    m: si,
    M: ai,
    p: st,
    q: it,
    Q: Ve,
    s: ze,
    S: oi,
    u: ci,
    U: li,
    V: ui,
    w: fi,
    W: hi,
    x: null,
    X: null,
    y: di,
    Y: gi,
    Z: ki,
    "%": Ne
  }, Q = {
    a: D,
    A: v,
    b: o,
    B: d,
    c: m,
    d: Ie,
    e: Ie,
    f: Ar,
    g: Ae,
    G: Ee,
    H: We,
    I: We,
    j: Yr,
    L: Er,
    m: Ur,
    M: Fr,
    p: Y,
    q: Sr,
    Q: Wr,
    s: Or,
    S: Lr,
    u: wr,
    U: Cr,
    V: Dr,
    w: xr,
    W: Mr,
    x: u,
    X: _,
    y: Ae,
    Y: Ee,
    Z: _r,
    "%": Ir
  };
  B.x = b(n, B), B.X = b(r, B), B.c = b(e, B), Z.x = b(n, Z), Z.X = b(r, Z), Z.c = b(e, Z);
  function b(p, E) {
    return function(M) {
      var l = [], R = -1, N = 0, j = p.length, J, et, Ut;
      for (M instanceof Date || (M = /* @__PURE__ */ new Date(+M)); ++R < j; )
        p.charCodeAt(R) === 37 && (l.push(p.slice(N, R)), (et = Le[J = p.charAt(++R)]) != null ? J = p.charAt(++R) : et = J === "e" ? " " : "0", (Ut = E[J]) && (J = Ut(M, et)), l.push(J), N = R + 1);
      return l.push(p.slice(N, R)), l.join("");
    };
  }
  function A(p, E) {
    return function(M) {
      var l = Yt(1900, void 0, 1), R = T(l, p, M += "", 0), N, j;
      if (R != M.length)
        return null;
      if ("Q" in l)
        return new Date(l.Q);
      if ("s" in l)
        return new Date(l.s * 1e3 + ("L" in l ? l.L : 0));
      if (E && !("Z" in l) && (l.Z = 0), "p" in l && (l.H = l.H % 12 + l.p * 12), l.m === void 0 && (l.m = "q" in l ? l.q : 0), "V" in l) {
        if (l.V < 1 || l.V > 53)
          return null;
        "w" in l || (l.w = 1), "Z" in l ? (N = le(Yt(l.y, 0, 1)), j = N.getUTCDay(), N = j > 4 || j === 0 ? jt.ceil(N) : jt(N), N = Te.offset(N, (l.V - 1) * 7), l.y = N.getUTCFullYear(), l.m = N.getUTCMonth(), l.d = N.getUTCDate() + (l.w + 6) % 7) : (N = ce(Yt(l.y, 0, 1)), j = N.getDay(), N = j > 4 || j === 0 ? It.ceil(N) : It(N), N = yt.offset(N, (l.V - 1) * 7), l.y = N.getFullYear(), l.m = N.getMonth(), l.d = N.getDate() + (l.w + 6) % 7);
      } else
        ("W" in l || "U" in l) && ("w" in l || (l.w = "u" in l ? l.u % 7 : "W" in l ? 1 : 0), j = "Z" in l ? le(Yt(l.y, 0, 1)).getUTCDay() : ce(Yt(l.y, 0, 1)).getDay(), l.m = 0, l.d = "W" in l ? (l.w + 6) % 7 + l.W * 7 - (j + 5) % 7 : l.w + l.U * 7 - (j + 6) % 7);
      return "Z" in l ? (l.H += l.Z / 100 | 0, l.M += l.Z % 100, le(l)) : ce(l);
    };
  }
  function T(p, E, M, l) {
    for (var R = 0, N = E.length, j = M.length, J, et; R < N; ) {
      if (l >= j)
        return -1;
      if (J = E.charCodeAt(R++), J === 37) {
        if (J = E.charAt(R++), et = Q[J in Le ? E.charAt(R++) : J], !et || (l = et(p, M, l)) < 0)
          return -1;
      } else if (J != M.charCodeAt(l++))
        return -1;
    }
    return l;
  }
  function Y(p, E, M) {
    var l = k.exec(E.slice(M));
    return l ? (p.p = C.get(l[0].toLowerCase()), M + l[0].length) : -1;
  }
  function D(p, E, M) {
    var l = x.exec(E.slice(M));
    return l ? (p.w = q.get(l[0].toLowerCase()), M + l[0].length) : -1;
  }
  function v(p, E, M) {
    var l = F.exec(E.slice(M));
    return l ? (p.w = w.get(l[0].toLowerCase()), M + l[0].length) : -1;
  }
  function o(p, E, M) {
    var l = O.exec(E.slice(M));
    return l ? (p.m = W.get(l[0].toLowerCase()), M + l[0].length) : -1;
  }
  function d(p, E, M) {
    var l = g.exec(E.slice(M));
    return l ? (p.m = L.get(l[0].toLowerCase()), M + l[0].length) : -1;
  }
  function m(p, E, M) {
    return T(p, e, E, M);
  }
  function u(p, E, M) {
    return T(p, n, E, M);
  }
  function _(p, E, M) {
    return T(p, r, E, M);
  }
  function c(p) {
    return a[p.getDay()];
  }
  function X(p) {
    return s[p.getDay()];
  }
  function f(p) {
    return S[p.getMonth()];
  }
  function h(p) {
    return y[p.getMonth()];
  }
  function U(p) {
    return i[+(p.getHours() >= 12)];
  }
  function G(p) {
    return 1 + ~~(p.getMonth() / 3);
  }
  function H(p) {
    return a[p.getUTCDay()];
  }
  function V(p) {
    return s[p.getUTCDay()];
  }
  function I(p) {
    return S[p.getUTCMonth()];
  }
  function z(p) {
    return y[p.getUTCMonth()];
  }
  function st(p) {
    return i[+(p.getUTCHours() >= 12)];
  }
  function it(p) {
    return 1 + ~~(p.getUTCMonth() / 3);
  }
  return {
    format: function(p) {
      var E = b(p += "", B);
      return E.toString = function() {
        return p;
      }, E;
    },
    parse: function(p) {
      var E = A(p += "", !1);
      return E.toString = function() {
        return p;
      }, E;
    },
    utcFormat: function(p) {
      var E = b(p += "", Z);
      return E.toString = function() {
        return p;
      }, E;
    },
    utcParse: function(p) {
      var E = A(p += "", !0);
      return E.toString = function() {
        return p;
      }, E;
    }
  };
}
var Le = { "-": "", _: " ", 0: "0" }, tt = /^\s*\d+/, Tr = /^%/, br = /[\\^$*+?|[\]().{}]/g;
function P(t, e, n) {
  var r = t < 0 ? "-" : "", i = (r ? -t : t) + "", s = i.length;
  return r + (s < n ? new Array(n - s + 1).join(e) + i : i);
}
function vr(t) {
  return t.replace(br, "\\$&");
}
function Ft(t) {
  return new RegExp("^(?:" + t.map(vr).join("|") + ")", "i");
}
function Lt(t) {
  return new Map(t.map((e, n) => [e.toLowerCase(), n]));
}
function xr(t, e, n) {
  var r = tt.exec(e.slice(n, n + 1));
  return r ? (t.w = +r[0], n + r[0].length) : -1;
}
function wr(t, e, n) {
  var r = tt.exec(e.slice(n, n + 1));
  return r ? (t.u = +r[0], n + r[0].length) : -1;
}
function Cr(t, e, n) {
  var r = tt.exec(e.slice(n, n + 2));
  return r ? (t.U = +r[0], n + r[0].length) : -1;
}
function Dr(t, e, n) {
  var r = tt.exec(e.slice(n, n + 2));
  return r ? (t.V = +r[0], n + r[0].length) : -1;
}
function Mr(t, e, n) {
  var r = tt.exec(e.slice(n, n + 2));
  return r ? (t.W = +r[0], n + r[0].length) : -1;
}
function Ee(t, e, n) {
  var r = tt.exec(e.slice(n, n + 4));
  return r ? (t.y = +r[0], n + r[0].length) : -1;
}
function Ae(t, e, n) {
  var r = tt.exec(e.slice(n, n + 2));
  return r ? (t.y = +r[0] + (+r[0] > 68 ? 1900 : 2e3), n + r[0].length) : -1;
}
function _r(t, e, n) {
  var r = /^(Z)|([+-]\d\d)(?::?(\d\d))?/.exec(e.slice(n, n + 6));
  return r ? (t.Z = r[1] ? 0 : -(r[2] + (r[3] || "00")), n + r[0].length) : -1;
}
function Sr(t, e, n) {
  var r = tt.exec(e.slice(n, n + 1));
  return r ? (t.q = r[0] * 3 - 3, n + r[0].length) : -1;
}
function Ur(t, e, n) {
  var r = tt.exec(e.slice(n, n + 2));
  return r ? (t.m = r[0] - 1, n + r[0].length) : -1;
}
function Ie(t, e, n) {
  var r = tt.exec(e.slice(n, n + 2));
  return r ? (t.d = +r[0], n + r[0].length) : -1;
}
function Yr(t, e, n) {
  var r = tt.exec(e.slice(n, n + 3));
  return r ? (t.m = 0, t.d = +r[0], n + r[0].length) : -1;
}
function We(t, e, n) {
  var r = tt.exec(e.slice(n, n + 2));
  return r ? (t.H = +r[0], n + r[0].length) : -1;
}
function Fr(t, e, n) {
  var r = tt.exec(e.slice(n, n + 2));
  return r ? (t.M = +r[0], n + r[0].length) : -1;
}
function Lr(t, e, n) {
  var r = tt.exec(e.slice(n, n + 2));
  return r ? (t.S = +r[0], n + r[0].length) : -1;
}
function Er(t, e, n) {
  var r = tt.exec(e.slice(n, n + 3));
  return r ? (t.L = +r[0], n + r[0].length) : -1;
}
function Ar(t, e, n) {
  var r = tt.exec(e.slice(n, n + 6));
  return r ? (t.L = Math.floor(r[0] / 1e3), n + r[0].length) : -1;
}
function Ir(t, e, n) {
  var r = Tr.exec(e.slice(n, n + 1));
  return r ? n + r[0].length : -1;
}
function Wr(t, e, n) {
  var r = tt.exec(e.slice(n));
  return r ? (t.Q = +r[0], n + r[0].length) : -1;
}
function Or(t, e, n) {
  var r = tt.exec(e.slice(n));
  return r ? (t.s = +r[0], n + r[0].length) : -1;
}
function Oe(t, e) {
  return P(t.getDate(), e, 2);
}
function Hr(t, e) {
  return P(t.getHours(), e, 2);
}
function Nr(t, e) {
  return P(t.getHours() % 12 || 12, e, 2);
}
function Vr(t, e) {
  return P(1 + yt.count(mt(t), t), e, 3);
}
function cn(t, e) {
  return P(t.getMilliseconds(), e, 3);
}
function zr(t, e) {
  return cn(t, e) + "000";
}
function Pr(t, e) {
  return P(t.getMonth() + 1, e, 2);
}
function Rr(t, e) {
  return P(t.getMinutes(), e, 2);
}
function Br(t, e) {
  return P(t.getSeconds(), e, 2);
}
function Zr(t) {
  var e = t.getDay();
  return e === 0 ? 7 : e;
}
function Xr(t, e) {
  return P(Ot.count(mt(t) - 1, t), e, 2);
}
function ln(t) {
  var e = t.getDay();
  return e >= 4 || e === 0 ? kt(t) : kt.ceil(t);
}
function qr(t, e) {
  return t = ln(t), P(kt.count(mt(t), t) + (mt(t).getDay() === 4), e, 2);
}
function Gr(t) {
  return t.getDay();
}
function jr(t, e) {
  return P(It.count(mt(t) - 1, t), e, 2);
}
function Qr(t, e) {
  return P(t.getFullYear() % 100, e, 2);
}
function Jr(t, e) {
  return t = ln(t), P(t.getFullYear() % 100, e, 2);
}
function Kr(t, e) {
  return P(t.getFullYear() % 1e4, e, 4);
}
function $r(t, e) {
  var n = t.getDay();
  return t = n >= 4 || n === 0 ? kt(t) : kt.ceil(t), P(t.getFullYear() % 1e4, e, 4);
}
function ti(t) {
  var e = t.getTimezoneOffset();
  return (e > 0 ? "-" : (e *= -1, "+")) + P(e / 60 | 0, "0", 2) + P(e % 60, "0", 2);
}
function He(t, e) {
  return P(t.getUTCDate(), e, 2);
}
function ei(t, e) {
  return P(t.getUTCHours(), e, 2);
}
function ni(t, e) {
  return P(t.getUTCHours() % 12 || 12, e, 2);
}
function ri(t, e) {
  return P(1 + Te.count(pt(t), t), e, 3);
}
function un(t, e) {
  return P(t.getUTCMilliseconds(), e, 3);
}
function ii(t, e) {
  return un(t, e) + "000";
}
function si(t, e) {
  return P(t.getUTCMonth() + 1, e, 2);
}
function ai(t, e) {
  return P(t.getUTCMinutes(), e, 2);
}
function oi(t, e) {
  return P(t.getUTCSeconds(), e, 2);
}
function ci(t) {
  var e = t.getUTCDay();
  return e === 0 ? 7 : e;
}
function li(t, e) {
  return P(on.count(pt(t) - 1, t), e, 2);
}
function fn(t) {
  var e = t.getUTCDay();
  return e >= 4 || e === 0 ? Mt(t) : Mt.ceil(t);
}
function ui(t, e) {
  return t = fn(t), P(Mt.count(pt(t), t) + (pt(t).getUTCDay() === 4), e, 2);
}
function fi(t) {
  return t.getUTCDay();
}
function hi(t, e) {
  return P(jt.count(pt(t) - 1, t), e, 2);
}
function di(t, e) {
  return P(t.getUTCFullYear() % 100, e, 2);
}
function mi(t, e) {
  return t = fn(t), P(t.getUTCFullYear() % 100, e, 2);
}
function gi(t, e) {
  return P(t.getUTCFullYear() % 1e4, e, 4);
}
function yi(t, e) {
  var n = t.getUTCDay();
  return t = n >= 4 || n === 0 ? Mt(t) : Mt.ceil(t), P(t.getUTCFullYear() % 1e4, e, 4);
}
function ki() {
  return "+0000";
}
function Ne() {
  return "%";
}
function Ve(t) {
  return +t;
}
function ze(t) {
  return Math.floor(+t / 1e3);
}
var vt, Qt;
pi({
  dateTime: "%x, %X",
  date: "%-m/%-d/%Y",
  time: "%-I:%M:%S %p",
  periods: ["AM", "PM"],
  days: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
  shortDays: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
  months: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
  shortMonths: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
});
function pi(t) {
  return vt = pr(t), Qt = vt.format, vt.parse, vt.utcFormat, vt.utcParse, vt;
}
function Ti(t) {
  return new Date(t);
}
function bi(t) {
  return t instanceof Date ? +t : +/* @__PURE__ */ new Date(+t);
}
function hn(t, e, n, r, i, s, a, y, S, k) {
  var C = Nn(), F = C.invert, w = C.domain, x = k(".%L"), q = k(":%S"), g = k("%I:%M"), L = k("%I %p"), O = k("%a %d"), W = k("%b %d"), B = k("%B"), Z = k("%Y");
  function Q(b) {
    return (S(b) < b ? x : y(b) < b ? q : a(b) < b ? g : s(b) < b ? L : r(b) < b ? i(b) < b ? O : W : n(b) < b ? B : Z)(b);
  }
  return C.invert = function(b) {
    return new Date(F(b));
  }, C.domain = function(b) {
    return arguments.length ? w(Array.from(b, bi)) : w().map(Ti);
  }, C.ticks = function(b) {
    var A = w();
    return t(A[0], A[A.length - 1], b ?? 10);
  }, C.tickFormat = function(b, A) {
    return A == null ? Q : k(A);
  }, C.nice = function(b) {
    var A = w();
    return (!b || typeof b.range != "function") && (b = e(A[0], A[A.length - 1], b ?? 10)), b ? w(ar(A, b)) : C;
  }, C.copy = function() {
    return Vn(C, hn(t, e, n, r, i, s, a, y, S, k));
  }, C;
}
function vi() {
  return Pn.apply(hn(yr, kr, mt, Wt, Ot, yt, At, Et, gt, Qt).domain([new Date(2e3, 0, 1), new Date(2e3, 0, 2)]), arguments);
}
var he = function() {
  var t = function(v, o, d, m) {
    for (d = d || {}, m = v.length; m--; d[v[m]] = o)
      ;
    return d;
  }, e = [6, 8, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 32, 33, 35, 37], n = [1, 25], r = [1, 26], i = [1, 27], s = [1, 28], a = [1, 29], y = [1, 30], S = [1, 31], k = [1, 9], C = [1, 10], F = [1, 11], w = [1, 12], x = [1, 13], q = [1, 14], g = [1, 15], L = [1, 16], O = [1, 18], W = [1, 19], B = [1, 20], Z = [1, 21], Q = [1, 22], b = [1, 24], A = [1, 32], T = {
    trace: function() {
    },
    yy: {},
    symbols_: { error: 2, start: 3, gantt: 4, document: 5, EOF: 6, line: 7, SPACE: 8, statement: 9, NL: 10, weekday: 11, weekday_monday: 12, weekday_tuesday: 13, weekday_wednesday: 14, weekday_thursday: 15, weekday_friday: 16, weekday_saturday: 17, weekday_sunday: 18, dateFormat: 19, inclusiveEndDates: 20, topAxis: 21, axisFormat: 22, tickInterval: 23, excludes: 24, includes: 25, todayMarker: 26, title: 27, acc_title: 28, acc_title_value: 29, acc_descr: 30, acc_descr_value: 31, acc_descr_multiline_value: 32, section: 33, clickStatement: 34, taskTxt: 35, taskData: 36, click: 37, callbackname: 38, callbackargs: 39, href: 40, clickStatementDebug: 41, $accept: 0, $end: 1 },
    terminals_: { 2: "error", 4: "gantt", 6: "EOF", 8: "SPACE", 10: "NL", 12: "weekday_monday", 13: "weekday_tuesday", 14: "weekday_wednesday", 15: "weekday_thursday", 16: "weekday_friday", 17: "weekday_saturday", 18: "weekday_sunday", 19: "dateFormat", 20: "inclusiveEndDates", 21: "topAxis", 22: "axisFormat", 23: "tickInterval", 24: "excludes", 25: "includes", 26: "todayMarker", 27: "title", 28: "acc_title", 29: "acc_title_value", 30: "acc_descr", 31: "acc_descr_value", 32: "acc_descr_multiline_value", 33: "section", 35: "taskTxt", 36: "taskData", 37: "click", 38: "callbackname", 39: "callbackargs", 40: "href" },
    productions_: [0, [3, 3], [5, 0], [5, 2], [7, 2], [7, 1], [7, 1], [7, 1], [11, 1], [11, 1], [11, 1], [11, 1], [11, 1], [11, 1], [11, 1], [9, 1], [9, 1], [9, 1], [9, 1], [9, 1], [9, 1], [9, 1], [9, 1], [9, 1], [9, 1], [9, 2], [9, 2], [9, 1], [9, 1], [9, 1], [9, 2], [34, 2], [34, 3], [34, 3], [34, 4], [34, 3], [34, 4], [34, 2], [41, 2], [41, 3], [41, 3], [41, 4], [41, 3], [41, 4], [41, 2]],
    performAction: function(o, d, m, u, _, c, X) {
      var f = c.length - 1;
      switch (_) {
        case 1:
          return c[f - 1];
        case 2:
          this.$ = [];
          break;
        case 3:
          c[f - 1].push(c[f]), this.$ = c[f - 1];
          break;
        case 4:
        case 5:
          this.$ = c[f];
          break;
        case 6:
        case 7:
          this.$ = [];
          break;
        case 8:
          u.setWeekday("monday");
          break;
        case 9:
          u.setWeekday("tuesday");
          break;
        case 10:
          u.setWeekday("wednesday");
          break;
        case 11:
          u.setWeekday("thursday");
          break;
        case 12:
          u.setWeekday("friday");
          break;
        case 13:
          u.setWeekday("saturday");
          break;
        case 14:
          u.setWeekday("sunday");
          break;
        case 15:
          u.setDateFormat(c[f].substr(11)), this.$ = c[f].substr(11);
          break;
        case 16:
          u.enableInclusiveEndDates(), this.$ = c[f].substr(18);
          break;
        case 17:
          u.TopAxis(), this.$ = c[f].substr(8);
          break;
        case 18:
          u.setAxisFormat(c[f].substr(11)), this.$ = c[f].substr(11);
          break;
        case 19:
          u.setTickInterval(c[f].substr(13)), this.$ = c[f].substr(13);
          break;
        case 20:
          u.setExcludes(c[f].substr(9)), this.$ = c[f].substr(9);
          break;
        case 21:
          u.setIncludes(c[f].substr(9)), this.$ = c[f].substr(9);
          break;
        case 22:
          u.setTodayMarker(c[f].substr(12)), this.$ = c[f].substr(12);
          break;
        case 24:
          u.setDiagramTitle(c[f].substr(6)), this.$ = c[f].substr(6);
          break;
        case 25:
          this.$ = c[f].trim(), u.setAccTitle(this.$);
          break;
        case 26:
        case 27:
          this.$ = c[f].trim(), u.setAccDescription(this.$);
          break;
        case 28:
          u.addSection(c[f].substr(8)), this.$ = c[f].substr(8);
          break;
        case 30:
          u.addTask(c[f - 1], c[f]), this.$ = "task";
          break;
        case 31:
          this.$ = c[f - 1], u.setClickEvent(c[f - 1], c[f], null);
          break;
        case 32:
          this.$ = c[f - 2], u.setClickEvent(c[f - 2], c[f - 1], c[f]);
          break;
        case 33:
          this.$ = c[f - 2], u.setClickEvent(c[f - 2], c[f - 1], null), u.setLink(c[f - 2], c[f]);
          break;
        case 34:
          this.$ = c[f - 3], u.setClickEvent(c[f - 3], c[f - 2], c[f - 1]), u.setLink(c[f - 3], c[f]);
          break;
        case 35:
          this.$ = c[f - 2], u.setClickEvent(c[f - 2], c[f], null), u.setLink(c[f - 2], c[f - 1]);
          break;
        case 36:
          this.$ = c[f - 3], u.setClickEvent(c[f - 3], c[f - 1], c[f]), u.setLink(c[f - 3], c[f - 2]);
          break;
        case 37:
          this.$ = c[f - 1], u.setLink(c[f - 1], c[f]);
          break;
        case 38:
        case 44:
          this.$ = c[f - 1] + " " + c[f];
          break;
        case 39:
        case 40:
        case 42:
          this.$ = c[f - 2] + " " + c[f - 1] + " " + c[f];
          break;
        case 41:
        case 43:
          this.$ = c[f - 3] + " " + c[f - 2] + " " + c[f - 1] + " " + c[f];
          break;
      }
    },
    table: [{ 3: 1, 4: [1, 2] }, { 1: [3] }, t(e, [2, 2], { 5: 3 }), { 6: [1, 4], 7: 5, 8: [1, 6], 9: 7, 10: [1, 8], 11: 17, 12: n, 13: r, 14: i, 15: s, 16: a, 17: y, 18: S, 19: k, 20: C, 21: F, 22: w, 23: x, 24: q, 25: g, 26: L, 27: O, 28: W, 30: B, 32: Z, 33: Q, 34: 23, 35: b, 37: A }, t(e, [2, 7], { 1: [2, 1] }), t(e, [2, 3]), { 9: 33, 11: 17, 12: n, 13: r, 14: i, 15: s, 16: a, 17: y, 18: S, 19: k, 20: C, 21: F, 22: w, 23: x, 24: q, 25: g, 26: L, 27: O, 28: W, 30: B, 32: Z, 33: Q, 34: 23, 35: b, 37: A }, t(e, [2, 5]), t(e, [2, 6]), t(e, [2, 15]), t(e, [2, 16]), t(e, [2, 17]), t(e, [2, 18]), t(e, [2, 19]), t(e, [2, 20]), t(e, [2, 21]), t(e, [2, 22]), t(e, [2, 23]), t(e, [2, 24]), { 29: [1, 34] }, { 31: [1, 35] }, t(e, [2, 27]), t(e, [2, 28]), t(e, [2, 29]), { 36: [1, 36] }, t(e, [2, 8]), t(e, [2, 9]), t(e, [2, 10]), t(e, [2, 11]), t(e, [2, 12]), t(e, [2, 13]), t(e, [2, 14]), { 38: [1, 37], 40: [1, 38] }, t(e, [2, 4]), t(e, [2, 25]), t(e, [2, 26]), t(e, [2, 30]), t(e, [2, 31], { 39: [1, 39], 40: [1, 40] }), t(e, [2, 37], { 38: [1, 41] }), t(e, [2, 32], { 40: [1, 42] }), t(e, [2, 33]), t(e, [2, 35], { 39: [1, 43] }), t(e, [2, 34]), t(e, [2, 36])],
    defaultActions: {},
    parseError: function(o, d) {
      if (d.recoverable)
        this.trace(o);
      else {
        var m = new Error(o);
        throw m.hash = d, m;
      }
    },
    parse: function(o) {
      var d = this, m = [0], u = [], _ = [null], c = [], X = this.table, f = "", h = 0, U = 0, G = 2, H = 1, V = c.slice.call(arguments, 1), I = Object.create(this.lexer), z = { yy: {} };
      for (var st in this.yy)
        Object.prototype.hasOwnProperty.call(this.yy, st) && (z.yy[st] = this.yy[st]);
      I.setInput(o, z.yy), z.yy.lexer = I, z.yy.parser = this, typeof I.yylloc > "u" && (I.yylloc = {});
      var it = I.yylloc;
      c.push(it);
      var p = I.options && I.options.ranges;
      typeof z.yy.parseError == "function" ? this.parseError = z.yy.parseError : this.parseError = Object.getPrototypeOf(this).parseError;
      function E() {
        var ct;
        return ct = u.pop() || I.lex() || H, typeof ct != "number" && (ct instanceof Array && (u = ct, ct = u.pop()), ct = d.symbols_[ct] || ct), ct;
      }
      for (var M, l, R, N, j = {}, J, et, Ut, zt; ; ) {
        if (l = m[m.length - 1], this.defaultActions[l] ? R = this.defaultActions[l] : ((M === null || typeof M > "u") && (M = E()), R = X[l] && X[l][M]), typeof R > "u" || !R.length || !R[0]) {
          var Kt = "";
          zt = [];
          for (J in X[l])
            this.terminals_[J] && J > G && zt.push("'" + this.terminals_[J] + "'");
          I.showPosition ? Kt = "Parse error on line " + (h + 1) + `:
` + I.showPosition() + `
Expecting ` + zt.join(", ") + ", got '" + (this.terminals_[M] || M) + "'" : Kt = "Parse error on line " + (h + 1) + ": Unexpected " + (M == H ? "end of input" : "'" + (this.terminals_[M] || M) + "'"), this.parseError(Kt, {
            text: I.match,
            token: this.terminals_[M] || M,
            line: I.yylineno,
            loc: it,
            expected: zt
          });
        }
        if (R[0] instanceof Array && R.length > 1)
          throw new Error("Parse Error: multiple actions possible at state: " + l + ", token: " + M);
        switch (R[0]) {
          case 1:
            m.push(M), _.push(I.yytext), c.push(I.yylloc), m.push(R[1]), M = null, U = I.yyleng, f = I.yytext, h = I.yylineno, it = I.yylloc;
            break;
          case 2:
            if (et = this.productions_[R[1]][1], j.$ = _[_.length - et], j._$ = {
              first_line: c[c.length - (et || 1)].first_line,
              last_line: c[c.length - 1].last_line,
              first_column: c[c.length - (et || 1)].first_column,
              last_column: c[c.length - 1].last_column
            }, p && (j._$.range = [
              c[c.length - (et || 1)].range[0],
              c[c.length - 1].range[1]
            ]), N = this.performAction.apply(j, [
              f,
              U,
              h,
              z.yy,
              R[1],
              _,
              c
            ].concat(V)), typeof N < "u")
              return N;
            et && (m = m.slice(0, -1 * et * 2), _ = _.slice(0, -1 * et), c = c.slice(0, -1 * et)), m.push(this.productions_[R[1]][0]), _.push(j.$), c.push(j._$), Ut = X[m[m.length - 2]][m[m.length - 1]], m.push(Ut);
            break;
          case 3:
            return !0;
        }
      }
      return !0;
    }
  }, Y = function() {
    var v = {
      EOF: 1,
      parseError: function(d, m) {
        if (this.yy.parser)
          this.yy.parser.parseError(d, m);
        else
          throw new Error(d);
      },
      // resets the lexer, sets new input
      setInput: function(o, d) {
        return this.yy = d || this.yy || {}, this._input = o, this._more = this._backtrack = this.done = !1, this.yylineno = this.yyleng = 0, this.yytext = this.matched = this.match = "", this.conditionStack = ["INITIAL"], this.yylloc = {
          first_line: 1,
          first_column: 0,
          last_line: 1,
          last_column: 0
        }, this.options.ranges && (this.yylloc.range = [0, 0]), this.offset = 0, this;
      },
      // consumes and returns one char from the input
      input: function() {
        var o = this._input[0];
        this.yytext += o, this.yyleng++, this.offset++, this.match += o, this.matched += o;
        var d = o.match(/(?:\r\n?|\n).*/g);
        return d ? (this.yylineno++, this.yylloc.last_line++) : this.yylloc.last_column++, this.options.ranges && this.yylloc.range[1]++, this._input = this._input.slice(1), o;
      },
      // unshifts one char (or a string) into the input
      unput: function(o) {
        var d = o.length, m = o.split(/(?:\r\n?|\n)/g);
        this._input = o + this._input, this.yytext = this.yytext.substr(0, this.yytext.length - d), this.offset -= d;
        var u = this.match.split(/(?:\r\n?|\n)/g);
        this.match = this.match.substr(0, this.match.length - 1), this.matched = this.matched.substr(0, this.matched.length - 1), m.length - 1 && (this.yylineno -= m.length - 1);
        var _ = this.yylloc.range;
        return this.yylloc = {
          first_line: this.yylloc.first_line,
          last_line: this.yylineno + 1,
          first_column: this.yylloc.first_column,
          last_column: m ? (m.length === u.length ? this.yylloc.first_column : 0) + u[u.length - m.length].length - m[0].length : this.yylloc.first_column - d
        }, this.options.ranges && (this.yylloc.range = [_[0], _[0] + this.yyleng - d]), this.yyleng = this.yytext.length, this;
      },
      // When called from action, caches matched text and appends it on next action
      more: function() {
        return this._more = !0, this;
      },
      // When called from action, signals the lexer that this rule fails to match the input, so the next matching rule (regex) should be tested instead.
      reject: function() {
        if (this.options.backtrack_lexer)
          this._backtrack = !0;
        else
          return this.parseError("Lexical error on line " + (this.yylineno + 1) + `. You can only invoke reject() in the lexer when the lexer is of the backtracking persuasion (options.backtrack_lexer = true).
` + this.showPosition(), {
            text: "",
            token: null,
            line: this.yylineno
          });
        return this;
      },
      // retain first n characters of the match
      less: function(o) {
        this.unput(this.match.slice(o));
      },
      // displays already matched input, i.e. for error messages
      pastInput: function() {
        var o = this.matched.substr(0, this.matched.length - this.match.length);
        return (o.length > 20 ? "..." : "") + o.substr(-20).replace(/\n/g, "");
      },
      // displays upcoming input, i.e. for error messages
      upcomingInput: function() {
        var o = this.match;
        return o.length < 20 && (o += this._input.substr(0, 20 - o.length)), (o.substr(0, 20) + (o.length > 20 ? "..." : "")).replace(/\n/g, "");
      },
      // displays the character position where the lexing error occurred, i.e. for error messages
      showPosition: function() {
        var o = this.pastInput(), d = new Array(o.length + 1).join("-");
        return o + this.upcomingInput() + `
` + d + "^";
      },
      // test the lexed token: return FALSE when not a match, otherwise return token
      test_match: function(o, d) {
        var m, u, _;
        if (this.options.backtrack_lexer && (_ = {
          yylineno: this.yylineno,
          yylloc: {
            first_line: this.yylloc.first_line,
            last_line: this.last_line,
            first_column: this.yylloc.first_column,
            last_column: this.yylloc.last_column
          },
          yytext: this.yytext,
          match: this.match,
          matches: this.matches,
          matched: this.matched,
          yyleng: this.yyleng,
          offset: this.offset,
          _more: this._more,
          _input: this._input,
          yy: this.yy,
          conditionStack: this.conditionStack.slice(0),
          done: this.done
        }, this.options.ranges && (_.yylloc.range = this.yylloc.range.slice(0))), u = o[0].match(/(?:\r\n?|\n).*/g), u && (this.yylineno += u.length), this.yylloc = {
          first_line: this.yylloc.last_line,
          last_line: this.yylineno + 1,
          first_column: this.yylloc.last_column,
          last_column: u ? u[u.length - 1].length - u[u.length - 1].match(/\r?\n?/)[0].length : this.yylloc.last_column + o[0].length
        }, this.yytext += o[0], this.match += o[0], this.matches = o, this.yyleng = this.yytext.length, this.options.ranges && (this.yylloc.range = [this.offset, this.offset += this.yyleng]), this._more = !1, this._backtrack = !1, this._input = this._input.slice(o[0].length), this.matched += o[0], m = this.performAction.call(this, this.yy, this, d, this.conditionStack[this.conditionStack.length - 1]), this.done && this._input && (this.done = !1), m)
          return m;
        if (this._backtrack) {
          for (var c in _)
            this[c] = _[c];
          return !1;
        }
        return !1;
      },
      // return next match in input
      next: function() {
        if (this.done)
          return this.EOF;
        this._input || (this.done = !0);
        var o, d, m, u;
        this._more || (this.yytext = "", this.match = "");
        for (var _ = this._currentRules(), c = 0; c < _.length; c++)
          if (m = this._input.match(this.rules[_[c]]), m && (!d || m[0].length > d[0].length)) {
            if (d = m, u = c, this.options.backtrack_lexer) {
              if (o = this.test_match(m, _[c]), o !== !1)
                return o;
              if (this._backtrack) {
                d = !1;
                continue;
              } else
                return !1;
            } else if (!this.options.flex)
              break;
          }
        return d ? (o = this.test_match(d, _[u]), o !== !1 ? o : !1) : this._input === "" ? this.EOF : this.parseError("Lexical error on line " + (this.yylineno + 1) + `. Unrecognized text.
` + this.showPosition(), {
          text: "",
          token: null,
          line: this.yylineno
        });
      },
      // return next match that has a token
      lex: function() {
        var d = this.next();
        return d || this.lex();
      },
      // activates a new lexer condition state (pushes the new lexer condition state onto the condition stack)
      begin: function(d) {
        this.conditionStack.push(d);
      },
      // pop the previously active lexer condition state off the condition stack
      popState: function() {
        var d = this.conditionStack.length - 1;
        return d > 0 ? this.conditionStack.pop() : this.conditionStack[0];
      },
      // produce the lexer rule set which is active for the currently active lexer condition state
      _currentRules: function() {
        return this.conditionStack.length && this.conditionStack[this.conditionStack.length - 1] ? this.conditions[this.conditionStack[this.conditionStack.length - 1]].rules : this.conditions.INITIAL.rules;
      },
      // return the currently active lexer condition state; when an index argument is provided it produces the N-th previous condition state, if available
      topState: function(d) {
        return d = this.conditionStack.length - 1 - Math.abs(d || 0), d >= 0 ? this.conditionStack[d] : "INITIAL";
      },
      // alias for begin(condition)
      pushState: function(d) {
        this.begin(d);
      },
      // return the number of states currently on the stack
      stateStackSize: function() {
        return this.conditionStack.length;
      },
      options: { "case-insensitive": !0 },
      performAction: function(d, m, u, _) {
        switch (u) {
          case 0:
            return this.begin("open_directive"), "open_directive";
          case 1:
            return this.begin("acc_title"), 28;
          case 2:
            return this.popState(), "acc_title_value";
          case 3:
            return this.begin("acc_descr"), 30;
          case 4:
            return this.popState(), "acc_descr_value";
          case 5:
            this.begin("acc_descr_multiline");
            break;
          case 6:
            this.popState();
            break;
          case 7:
            return "acc_descr_multiline_value";
          case 8:
            break;
          case 9:
            break;
          case 10:
            break;
          case 11:
            return 10;
          case 12:
            break;
          case 13:
            break;
          case 14:
            this.begin("href");
            break;
          case 15:
            this.popState();
            break;
          case 16:
            return 40;
          case 17:
            this.begin("callbackname");
            break;
          case 18:
            this.popState();
            break;
          case 19:
            this.popState(), this.begin("callbackargs");
            break;
          case 20:
            return 38;
          case 21:
            this.popState();
            break;
          case 22:
            return 39;
          case 23:
            this.begin("click");
            break;
          case 24:
            this.popState();
            break;
          case 25:
            return 37;
          case 26:
            return 4;
          case 27:
            return 19;
          case 28:
            return 20;
          case 29:
            return 21;
          case 30:
            return 22;
          case 31:
            return 23;
          case 32:
            return 25;
          case 33:
            return 24;
          case 34:
            return 26;
          case 35:
            return 12;
          case 36:
            return 13;
          case 37:
            return 14;
          case 38:
            return 15;
          case 39:
            return 16;
          case 40:
            return 17;
          case 41:
            return 18;
          case 42:
            return "date";
          case 43:
            return 27;
          case 44:
            return "accDescription";
          case 45:
            return 33;
          case 46:
            return 35;
          case 47:
            return 36;
          case 48:
            return ":";
          case 49:
            return 6;
          case 50:
            return "INVALID";
        }
      },
      rules: [/^(?:%%\{)/i, /^(?:accTitle\s*:\s*)/i, /^(?:(?!\n||)*[^\n]*)/i, /^(?:accDescr\s*:\s*)/i, /^(?:(?!\n||)*[^\n]*)/i, /^(?:accDescr\s*\{\s*)/i, /^(?:[\}])/i, /^(?:[^\}]*)/i, /^(?:%%(?!\{)*[^\n]*)/i, /^(?:[^\}]%%*[^\n]*)/i, /^(?:%%*[^\n]*[\n]*)/i, /^(?:[\n]+)/i, /^(?:\s+)/i, /^(?:%[^\n]*)/i, /^(?:href[\s]+["])/i, /^(?:["])/i, /^(?:[^"]*)/i, /^(?:call[\s]+)/i, /^(?:\([\s]*\))/i, /^(?:\()/i, /^(?:[^(]*)/i, /^(?:\))/i, /^(?:[^)]*)/i, /^(?:click[\s]+)/i, /^(?:[\s\n])/i, /^(?:[^\s\n]*)/i, /^(?:gantt\b)/i, /^(?:dateFormat\s[^#\n;]+)/i, /^(?:inclusiveEndDates\b)/i, /^(?:topAxis\b)/i, /^(?:axisFormat\s[^#\n;]+)/i, /^(?:tickInterval\s[^#\n;]+)/i, /^(?:includes\s[^#\n;]+)/i, /^(?:excludes\s[^#\n;]+)/i, /^(?:todayMarker\s[^\n;]+)/i, /^(?:weekday\s+monday\b)/i, /^(?:weekday\s+tuesday\b)/i, /^(?:weekday\s+wednesday\b)/i, /^(?:weekday\s+thursday\b)/i, /^(?:weekday\s+friday\b)/i, /^(?:weekday\s+saturday\b)/i, /^(?:weekday\s+sunday\b)/i, /^(?:\d\d\d\d-\d\d-\d\d\b)/i, /^(?:title\s[^\n]+)/i, /^(?:accDescription\s[^#\n;]+)/i, /^(?:section\s[^\n]+)/i, /^(?:[^:\n]+)/i, /^(?::[^#\n;]+)/i, /^(?::)/i, /^(?:$)/i, /^(?:.)/i],
      conditions: { acc_descr_multiline: { rules: [6, 7], inclusive: !1 }, acc_descr: { rules: [4], inclusive: !1 }, acc_title: { rules: [2], inclusive: !1 }, callbackargs: { rules: [21, 22], inclusive: !1 }, callbackname: { rules: [18, 19, 20], inclusive: !1 }, href: { rules: [15, 16], inclusive: !1 }, click: { rules: [24, 25], inclusive: !1 }, INITIAL: { rules: [0, 1, 3, 5, 8, 9, 10, 11, 12, 13, 14, 17, 23, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], inclusive: !0 } }
    };
    return v;
  }();
  T.lexer = Y;
  function D() {
    this.yy = {};
  }
  return D.prototype = T, T.Parser = D, new D();
}();
he.parser = he;
const xi = he;
var dn = { exports: {} };
(function(t, e) {
  (function(n, r) {
    t.exports = r();
  })(ye, function() {
    var n = "day";
    return function(r, i, s) {
      var a = function(k) {
        return k.add(4 - k.isoWeekday(), n);
      }, y = i.prototype;
      y.isoWeekYear = function() {
        return a(this).year();
      }, y.isoWeek = function(k) {
        if (!this.$utils().u(k))
          return this.add(7 * (k - this.isoWeek()), n);
        var C, F, w, x, q = a(this), g = (C = this.isoWeekYear(), F = this.$u, w = (F ? s.utc : s)().year(C).startOf("year"), x = 4 - w.isoWeekday(), w.isoWeekday() > 4 && (x += 7), w.add(x, n));
        return q.diff(g, "week") + 1;
      }, y.isoWeekday = function(k) {
        return this.$utils().u(k) ? this.day() || 7 : this.day(this.day() % 7 ? k : k - 7);
      };
      var S = y.startOf;
      y.startOf = function(k, C) {
        var F = this.$utils(), w = !!F.u(C) || C;
        return F.p(k) === "isoweek" ? w ? this.date(this.date() - (this.isoWeekday() - 1)).startOf("day") : this.date(this.date() - 1 - (this.isoWeekday() - 1) + 7).endOf("day") : S.bind(this)(k, C);
      };
    };
  });
})(dn);
var wi = dn.exports;
const Ci = /* @__PURE__ */ ke(wi);
var mn = { exports: {} };
(function(t, e) {
  (function(n, r) {
    t.exports = r();
  })(ye, function() {
    var n = { LTS: "h:mm:ss A", LT: "h:mm A", L: "MM/DD/YYYY", LL: "MMMM D, YYYY", LLL: "MMMM D, YYYY h:mm A", LLLL: "dddd, MMMM D, YYYY h:mm A" }, r = /(\[[^[]*\])|([-_:/.,()\s]+)|(A|a|YYYY|YY?|MM?M?M?|Do|DD?|hh?|HH?|mm?|ss?|S{1,3}|z|ZZ?)/g, i = /\d\d/, s = /\d\d?/, a = /\d*[^-_:/,()\s\d]+/, y = {}, S = function(g) {
      return (g = +g) + (g > 68 ? 1900 : 2e3);
    }, k = function(g) {
      return function(L) {
        this[g] = +L;
      };
    }, C = [/[+-]\d\d:?(\d\d)?|Z/, function(g) {
      (this.zone || (this.zone = {})).offset = function(L) {
        if (!L || L === "Z")
          return 0;
        var O = L.match(/([+-]|\d\d)/g), W = 60 * O[1] + (+O[2] || 0);
        return W === 0 ? 0 : O[0] === "+" ? -W : W;
      }(g);
    }], F = function(g) {
      var L = y[g];
      return L && (L.indexOf ? L : L.s.concat(L.f));
    }, w = function(g, L) {
      var O, W = y.meridiem;
      if (W) {
        for (var B = 1; B <= 24; B += 1)
          if (g.indexOf(W(B, 0, L)) > -1) {
            O = B > 12;
            break;
          }
      } else
        O = g === (L ? "pm" : "PM");
      return O;
    }, x = { A: [a, function(g) {
      this.afternoon = w(g, !1);
    }], a: [a, function(g) {
      this.afternoon = w(g, !0);
    }], S: [/\d/, function(g) {
      this.milliseconds = 100 * +g;
    }], SS: [i, function(g) {
      this.milliseconds = 10 * +g;
    }], SSS: [/\d{3}/, function(g) {
      this.milliseconds = +g;
    }], s: [s, k("seconds")], ss: [s, k("seconds")], m: [s, k("minutes")], mm: [s, k("minutes")], H: [s, k("hours")], h: [s, k("hours")], HH: [s, k("hours")], hh: [s, k("hours")], D: [s, k("day")], DD: [i, k("day")], Do: [a, function(g) {
      var L = y.ordinal, O = g.match(/\d+/);
      if (this.day = O[0], L)
        for (var W = 1; W <= 31; W += 1)
          L(W).replace(/\[|\]/g, "") === g && (this.day = W);
    }], M: [s, k("month")], MM: [i, k("month")], MMM: [a, function(g) {
      var L = F("months"), O = (F("monthsShort") || L.map(function(W) {
        return W.slice(0, 3);
      })).indexOf(g) + 1;
      if (O < 1)
        throw new Error();
      this.month = O % 12 || O;
    }], MMMM: [a, function(g) {
      var L = F("months").indexOf(g) + 1;
      if (L < 1)
        throw new Error();
      this.month = L % 12 || L;
    }], Y: [/[+-]?\d+/, k("year")], YY: [i, function(g) {
      this.year = S(g);
    }], YYYY: [/\d{4}/, k("year")], Z: C, ZZ: C };
    function q(g) {
      var L, O;
      L = g, O = y && y.formats;
      for (var W = (g = L.replace(/(\[[^\]]+])|(LTS?|l{1,4}|L{1,4})/g, function(Y, D, v) {
        var o = v && v.toUpperCase();
        return D || O[v] || n[v] || O[o].replace(/(\[[^\]]+])|(MMMM|MM|DD|dddd)/g, function(d, m, u) {
          return m || u.slice(1);
        });
      })).match(r), B = W.length, Z = 0; Z < B; Z += 1) {
        var Q = W[Z], b = x[Q], A = b && b[0], T = b && b[1];
        W[Z] = T ? { regex: A, parser: T } : Q.replace(/^\[|\]$/g, "");
      }
      return function(Y) {
        for (var D = {}, v = 0, o = 0; v < B; v += 1) {
          var d = W[v];
          if (typeof d == "string")
            o += d.length;
          else {
            var m = d.regex, u = d.parser, _ = Y.slice(o), c = m.exec(_)[0];
            u.call(D, c), Y = Y.replace(c, "");
          }
        }
        return function(X) {
          var f = X.afternoon;
          if (f !== void 0) {
            var h = X.hours;
            f ? h < 12 && (X.hours += 12) : h === 12 && (X.hours = 0), delete X.afternoon;
          }
        }(D), D;
      };
    }
    return function(g, L, O) {
      O.p.customParseFormat = !0, g && g.parseTwoDigitYear && (S = g.parseTwoDigitYear);
      var W = L.prototype, B = W.parse;
      W.parse = function(Z) {
        var Q = Z.date, b = Z.utc, A = Z.args;
        this.$u = b;
        var T = A[1];
        if (typeof T == "string") {
          var Y = A[2] === !0, D = A[3] === !0, v = Y || D, o = A[2];
          D && (o = A[2]), y = this.$locale(), !Y && o && (y = O.Ls[o]), this.$d = function(_, c, X) {
            try {
              if (["x", "X"].indexOf(c) > -1)
                return new Date((c === "X" ? 1e3 : 1) * _);
              var f = q(c)(_), h = f.year, U = f.month, G = f.day, H = f.hours, V = f.minutes, I = f.seconds, z = f.milliseconds, st = f.zone, it = /* @__PURE__ */ new Date(), p = G || (h || U ? 1 : it.getDate()), E = h || it.getFullYear(), M = 0;
              h && !U || (M = U > 0 ? U - 1 : it.getMonth());
              var l = H || 0, R = V || 0, N = I || 0, j = z || 0;
              return st ? new Date(Date.UTC(E, M, p, l, R, N, j + 60 * st.offset * 1e3)) : X ? new Date(Date.UTC(E, M, p, l, R, N, j)) : new Date(E, M, p, l, R, N, j);
            } catch {
              return /* @__PURE__ */ new Date("");
            }
          }(Q, T, b), this.init(), o && o !== !0 && (this.$L = this.locale(o).$L), v && Q != this.format(T) && (this.$d = /* @__PURE__ */ new Date("")), y = {};
        } else if (T instanceof Array)
          for (var d = T.length, m = 1; m <= d; m += 1) {
            A[1] = T[m - 1];
            var u = O.apply(this, A);
            if (u.isValid()) {
              this.$d = u.$d, this.$L = u.$L, this.init();
              break;
            }
            m === d && (this.$d = /* @__PURE__ */ new Date(""));
          }
        else
          B.call(this, Z);
      };
    };
  });
})(mn);
var Di = mn.exports;
const Mi = /* @__PURE__ */ ke(Di);
var gn = { exports: {} };
(function(t, e) {
  (function(n, r) {
    t.exports = r();
  })(ye, function() {
    return function(n, r) {
      var i = r.prototype, s = i.format;
      i.format = function(a) {
        var y = this, S = this.$locale();
        if (!this.isValid())
          return s.bind(this)(a);
        var k = this.$utils(), C = (a || "YYYY-MM-DDTHH:mm:ssZ").replace(/\[([^\]]+)]|Q|wo|ww|w|WW|W|zzz|z|gggg|GGGG|Do|X|x|k{1,2}|S/g, function(F) {
          switch (F) {
            case "Q":
              return Math.ceil((y.$M + 1) / 3);
            case "Do":
              return S.ordinal(y.$D);
            case "gggg":
              return y.weekYear();
            case "GGGG":
              return y.isoWeekYear();
            case "wo":
              return S.ordinal(y.week(), "W");
            case "w":
            case "ww":
              return k.s(y.week(), F === "w" ? 1 : 2, "0");
            case "W":
            case "WW":
              return k.s(y.isoWeek(), F === "W" ? 1 : 2, "0");
            case "k":
            case "kk":
              return k.s(String(y.$H === 0 ? 24 : y.$H), F === "k" ? 1 : 2, "0");
            case "X":
              return Math.floor(y.$d.getTime() / 1e3);
            case "x":
              return y.$d.getTime();
            case "z":
              return "[" + y.offsetName() + "]";
            case "zzz":
              return "[" + y.offsetName("long") + "]";
            default:
              return F;
          }
        });
        return s.bind(this)(C);
      };
    };
  });
})(gn);
var _i = gn.exports;
const Si = /* @__PURE__ */ ke(_i);
nt.extend(Ci);
nt.extend(Mi);
nt.extend(Si);
let at = "", be = "", ve, xe = "", Ht = [], Nt = [], we = {}, Ce = [], Jt = [], _t = "", De = "";
const yn = ["active", "done", "crit", "milestone"];
let Me = [], Vt = !1, _e = !1, Se = "sunday", de = 0;
const Ui = function() {
  Ce = [], Jt = [], _t = "", Me = [], Zt = 0, ge = void 0, Xt = void 0, K = [], at = "", be = "", De = "", ve = void 0, xe = "", Ht = [], Nt = [], Vt = !1, _e = !1, de = 0, we = {}, En(), Se = "sunday";
}, Yi = function(t) {
  be = t;
}, Fi = function() {
  return be;
}, Li = function(t) {
  ve = t;
}, Ei = function() {
  return ve;
}, Ai = function(t) {
  xe = t;
}, Ii = function() {
  return xe;
}, Wi = function(t) {
  at = t;
}, Oi = function() {
  Vt = !0;
}, Hi = function() {
  return Vt;
}, Ni = function() {
  _e = !0;
}, Vi = function() {
  return _e;
}, zi = function(t) {
  De = t;
}, Pi = function() {
  return De;
}, Ri = function() {
  return at;
}, Bi = function(t) {
  Ht = t.toLowerCase().split(/[\s,]+/);
}, Zi = function() {
  return Ht;
}, Xi = function(t) {
  Nt = t.toLowerCase().split(/[\s,]+/);
}, qi = function() {
  return Nt;
}, Gi = function() {
  return we;
}, ji = function(t) {
  _t = t, Ce.push(t);
}, Qi = function() {
  return Ce;
}, Ji = function() {
  let t = Pe();
  const e = 10;
  let n = 0;
  for (; !t && n < e; )
    t = Pe(), n++;
  return Jt = K, Jt;
}, kn = function(t, e, n, r) {
  return r.includes(t.format(e.trim())) ? !1 : t.isoWeekday() >= 6 && n.includes("weekends") || n.includes(t.format("dddd").toLowerCase()) ? !0 : n.includes(t.format(e.trim()));
}, Ki = function(t) {
  Se = t;
}, $i = function() {
  return Se;
}, pn = function(t, e, n, r) {
  if (!n.length || t.manualEndTime)
    return;
  let i;
  t.startTime instanceof Date ? i = nt(t.startTime) : i = nt(t.startTime, e, !0), i = i.add(1, "d");
  let s;
  t.endTime instanceof Date ? s = nt(t.endTime) : s = nt(t.endTime, e, !0);
  const [a, y] = ts(
    i,
    s,
    e,
    n,
    r
  );
  t.endTime = a.toDate(), t.renderEndTime = y;
}, ts = function(t, e, n, r, i) {
  let s = !1, a = null;
  for (; t <= e; )
    s || (a = e.toDate()), s = kn(t, n, r, i), s && (e = e.add(1, "d")), t = t.add(1, "d");
  return [e, a];
}, me = function(t, e, n) {
  n = n.trim();
  const i = /^after\s+([\d\w- ]+)/.exec(n.trim());
  if (i !== null) {
    let a = null;
    if (i[1].split(" ").forEach(function(y) {
      let S = St(y);
      S !== void 0 && (a ? S.endTime > a.endTime && (a = S) : a = S);
    }), a)
      return a.endTime;
    {
      const y = /* @__PURE__ */ new Date();
      return y.setHours(0, 0, 0, 0), y;
    }
  }
  let s = nt(n, e.trim(), !0);
  if (s.isValid())
    return s.toDate();
  {
    qt.debug("Invalid date:" + n), qt.debug("With date format:" + e.trim());
    const a = new Date(n);
    if (a === void 0 || isNaN(a.getTime()) || // WebKit browsers can mis-parse invalid dates to be ridiculously
    // huge numbers, e.g. new Date('202304') gets parsed as January 1, 202304.
    // This can cause virtually infinite loops while rendering, so for the
    // purposes of Gantt charts we'll just treat any date beyond 10,000 AD/BC as
    // invalid.
    a.getFullYear() < -1e4 || a.getFullYear() > 1e4)
      throw new Error("Invalid date:" + n);
    return a;
  }
}, Tn = function(t) {
  const e = /^(\d+(?:\.\d+)?)([Mdhmswy]|ms)$/.exec(t.trim());
  return e !== null ? [Number.parseFloat(e[1]), e[2]] : [NaN, "ms"];
}, bn = function(t, e, n, r = !1) {
  n = n.trim();
  let i = nt(n, e.trim(), !0);
  if (i.isValid())
    return r && (i = i.add(1, "d")), i.toDate();
  let s = nt(t);
  const [a, y] = Tn(n);
  if (!Number.isNaN(a)) {
    const S = s.add(a, y);
    S.isValid() && (s = S);
  }
  return s.toDate();
};
let Zt = 0;
const Ct = function(t) {
  return t === void 0 ? (Zt = Zt + 1, "task" + Zt) : t;
}, es = function(t, e) {
  let n;
  e.substr(0, 1) === ":" ? n = e.substr(1, e.length) : n = e;
  const r = n.split(","), i = {};
  Cn(r, i, yn);
  for (let a = 0; a < r.length; a++)
    r[a] = r[a].trim();
  let s = "";
  switch (r.length) {
    case 1:
      i.id = Ct(), i.startTime = t.endTime, s = r[0];
      break;
    case 2:
      i.id = Ct(), i.startTime = me(void 0, at, r[0]), s = r[1];
      break;
    case 3:
      i.id = Ct(r[0]), i.startTime = me(void 0, at, r[1]), s = r[2];
      break;
  }
  return s && (i.endTime = bn(i.startTime, at, s, Vt), i.manualEndTime = nt(s, "YYYY-MM-DD", !0).isValid(), pn(i, at, Nt, Ht)), i;
}, ns = function(t, e) {
  let n;
  e.substr(0, 1) === ":" ? n = e.substr(1, e.length) : n = e;
  const r = n.split(","), i = {};
  Cn(r, i, yn);
  for (let s = 0; s < r.length; s++)
    r[s] = r[s].trim();
  switch (r.length) {
    case 1:
      i.id = Ct(), i.startTime = {
        type: "prevTaskEnd",
        id: t
      }, i.endTime = {
        data: r[0]
      };
      break;
    case 2:
      i.id = Ct(), i.startTime = {
        type: "getStartDate",
        startData: r[0]
      }, i.endTime = {
        data: r[1]
      };
      break;
    case 3:
      i.id = Ct(r[0]), i.startTime = {
        type: "getStartDate",
        startData: r[1]
      }, i.endTime = {
        data: r[2]
      };
      break;
  }
  return i;
};
let ge, Xt, K = [];
const vn = {}, rs = function(t, e) {
  const n = {
    section: _t,
    type: _t,
    processed: !1,
    manualEndTime: !1,
    renderEndTime: null,
    raw: { data: e },
    task: t,
    classes: []
  }, r = ns(Xt, e);
  n.raw.startTime = r.startTime, n.raw.endTime = r.endTime, n.id = r.id, n.prevTaskId = Xt, n.active = r.active, n.done = r.done, n.crit = r.crit, n.milestone = r.milestone, n.order = de, de++;
  const i = K.push(n);
  Xt = n.id, vn[n.id] = i - 1;
}, St = function(t) {
  const e = vn[t];
  return K[e];
}, is = function(t, e) {
  const n = {
    section: _t,
    type: _t,
    description: t,
    task: t,
    classes: []
  }, r = es(ge, e);
  n.startTime = r.startTime, n.endTime = r.endTime, n.id = r.id, n.active = r.active, n.done = r.done, n.crit = r.crit, n.milestone = r.milestone, ge = n, Jt.push(n);
}, Pe = function() {
  const t = function(n) {
    const r = K[n];
    let i = "";
    switch (K[n].raw.startTime.type) {
      case "prevTaskEnd": {
        const s = St(r.prevTaskId);
        r.startTime = s.endTime;
        break;
      }
      case "getStartDate":
        i = me(void 0, at, K[n].raw.startTime.startData), i && (K[n].startTime = i);
        break;
    }
    return K[n].startTime && (K[n].endTime = bn(
      K[n].startTime,
      at,
      K[n].raw.endTime.data,
      Vt
    ), K[n].endTime && (K[n].processed = !0, K[n].manualEndTime = nt(
      K[n].raw.endTime.data,
      "YYYY-MM-DD",
      !0
    ).isValid(), pn(K[n], at, Nt, Ht))), K[n].processed;
  };
  let e = !0;
  for (const [n, r] of K.entries())
    t(n), e = e && r.processed;
  return e;
}, ss = function(t, e) {
  let n = e;
  xt().securityLevel !== "loose" && (n = An(e)), t.split(",").forEach(function(r) {
    St(r) !== void 0 && (wn(r, () => {
      window.open(n, "_self");
    }), we[r] = n);
  }), xn(t, "clickable");
}, xn = function(t, e) {
  t.split(",").forEach(function(n) {
    let r = St(n);
    r !== void 0 && r.classes.push(e);
  });
}, as = function(t, e, n) {
  if (xt().securityLevel !== "loose" || e === void 0)
    return;
  let r = [];
  if (typeof n == "string") {
    r = n.split(/,(?=(?:(?:[^"]*"){2})*[^"]*$)/);
    for (let s = 0; s < r.length; s++) {
      let a = r[s].trim();
      a.charAt(0) === '"' && a.charAt(a.length - 1) === '"' && (a = a.substr(1, a.length - 2)), r[s] = a;
    }
  }
  r.length === 0 && r.push(t), St(t) !== void 0 && wn(t, () => {
    In.runFunc(e, ...r);
  });
}, wn = function(t, e) {
  Me.push(
    function() {
      const n = document.querySelector(`[id="${t}"]`);
      n !== null && n.addEventListener("click", function() {
        e();
      });
    },
    function() {
      const n = document.querySelector(`[id="${t}-text"]`);
      n !== null && n.addEventListener("click", function() {
        e();
      });
    }
  );
}, os = function(t, e, n) {
  t.split(",").forEach(function(r) {
    as(r, e, n);
  }), xn(t, "clickable");
}, cs = function(t) {
  Me.forEach(function(e) {
    e(t);
  });
}, ls = {
  getConfig: () => xt().gantt,
  clear: Ui,
  setDateFormat: Wi,
  getDateFormat: Ri,
  enableInclusiveEndDates: Oi,
  endDatesAreInclusive: Hi,
  enableTopAxis: Ni,
  topAxisEnabled: Vi,
  setAxisFormat: Yi,
  getAxisFormat: Fi,
  setTickInterval: Li,
  getTickInterval: Ei,
  setTodayMarker: Ai,
  getTodayMarker: Ii,
  setAccTitle: _n,
  getAccTitle: Sn,
  setDiagramTitle: Un,
  getDiagramTitle: Yn,
  setDisplayMode: zi,
  getDisplayMode: Pi,
  setAccDescription: Fn,
  getAccDescription: Ln,
  addSection: ji,
  getSections: Qi,
  getTasks: Ji,
  addTask: rs,
  findTaskById: St,
  addTaskOrg: is,
  setIncludes: Bi,
  getIncludes: Zi,
  setExcludes: Xi,
  getExcludes: qi,
  setClickEvent: os,
  setLink: ss,
  getLinks: Gi,
  bindFunctions: cs,
  parseDuration: Tn,
  isInvalidDate: kn,
  setWeekday: Ki,
  getWeekday: $i
};
function Cn(t, e, n) {
  let r = !0;
  for (; r; )
    r = !1, n.forEach(function(i) {
      const s = "^\\s*" + i + "\\s*$", a = new RegExp(s);
      t[0].match(a) && (e[i] = !0, t.shift(1), r = !0);
    });
}
const us = function() {
  qt.debug("Something is calling, setConf, remove the call");
}, Re = {
  monday: It,
  tuesday: nn,
  wednesday: rn,
  thursday: kt,
  friday: sn,
  saturday: an,
  sunday: Ot
}, fs = (t, e) => {
  let n = [...t].map(() => -1 / 0), r = [...t].sort((s, a) => s.startTime - a.startTime || s.order - a.order), i = 0;
  for (const s of r)
    for (let a = 0; a < n.length; a++)
      if (s.startTime >= n[a]) {
        n[a] = s.endTime, s.order = a + e, a > i && (i = a);
        break;
      }
  return i;
};
let lt;
const hs = function(t, e, n, r) {
  const i = xt().gantt, s = xt().securityLevel;
  let a;
  s === "sandbox" && (a = Pt("#i" + e));
  const y = s === "sandbox" ? Pt(a.nodes()[0].contentDocument.body) : Pt("body"), S = s === "sandbox" ? a.nodes()[0].contentDocument : document, k = S.getElementById(e);
  lt = k.parentElement.offsetWidth, lt === void 0 && (lt = 1200), i.useWidth !== void 0 && (lt = i.useWidth);
  const C = r.db.getTasks();
  let F = [];
  for (const T of C)
    F.push(T.type);
  F = A(F);
  const w = {};
  let x = 2 * i.topPadding;
  if (r.db.getDisplayMode() === "compact" || i.displayMode === "compact") {
    const T = {};
    for (const D of C)
      T[D.section] === void 0 ? T[D.section] = [D] : T[D.section].push(D);
    let Y = 0;
    for (const D of Object.keys(T)) {
      const v = fs(T[D], Y) + 1;
      Y += v, x += v * (i.barHeight + i.barGap), w[D] = v;
    }
  } else {
    x += C.length * (i.barHeight + i.barGap);
    for (const T of F)
      w[T] = C.filter((Y) => Y.type === T).length;
  }
  k.setAttribute("viewBox", "0 0 " + lt + " " + x);
  const q = y.select(`[id="${e}"]`), g = vi().domain([
    Bn(C, function(T) {
      return T.startTime;
    }),
    Rn(C, function(T) {
      return T.endTime;
    })
  ]).rangeRound([0, lt - i.leftPadding - i.rightPadding]);
  function L(T, Y) {
    const D = T.startTime, v = Y.startTime;
    let o = 0;
    return D > v ? o = 1 : D < v && (o = -1), o;
  }
  C.sort(L), O(C, lt, x), Wn(q, x, lt, i.useMaxWidth), q.append("text").text(r.db.getDiagramTitle()).attr("x", lt / 2).attr("y", i.titleTopMargin).attr("class", "titleText");
  function O(T, Y, D) {
    const v = i.barHeight, o = v + i.barGap, d = i.topPadding, m = i.leftPadding, u = zn().domain([0, F.length]).range(["#00B9FA", "#F95002"]).interpolate(sr);
    B(
      o,
      d,
      m,
      Y,
      D,
      T,
      r.db.getExcludes(),
      r.db.getIncludes()
    ), Z(m, d, Y, D), W(T, o, d, m, v, u, Y), Q(o, d), b(m, d, Y, D);
  }
  function W(T, Y, D, v, o, d, m) {
    const _ = [...new Set(T.map((h) => h.order))].map((h) => T.find((U) => U.order === h));
    q.append("g").selectAll("rect").data(_).enter().append("rect").attr("x", 0).attr("y", function(h, U) {
      return U = h.order, U * Y + D - 2;
    }).attr("width", function() {
      return m - i.rightPadding / 2;
    }).attr("height", Y).attr("class", function(h) {
      for (const [U, G] of F.entries())
        if (h.type === G)
          return "section section" + U % i.numberSectionStyles;
      return "section section0";
    });
    const c = q.append("g").selectAll("rect").data(T).enter(), X = r.db.getLinks();
    if (c.append("rect").attr("id", function(h) {
      return h.id;
    }).attr("rx", 3).attr("ry", 3).attr("x", function(h) {
      return h.milestone ? g(h.startTime) + v + 0.5 * (g(h.endTime) - g(h.startTime)) - 0.5 * o : g(h.startTime) + v;
    }).attr("y", function(h, U) {
      return U = h.order, U * Y + D;
    }).attr("width", function(h) {
      return h.milestone ? o : g(h.renderEndTime || h.endTime) - g(h.startTime);
    }).attr("height", o).attr("transform-origin", function(h, U) {
      return U = h.order, (g(h.startTime) + v + 0.5 * (g(h.endTime) - g(h.startTime))).toString() + "px " + (U * Y + D + 0.5 * o).toString() + "px";
    }).attr("class", function(h) {
      const U = "task";
      let G = "";
      h.classes.length > 0 && (G = h.classes.join(" "));
      let H = 0;
      for (const [I, z] of F.entries())
        h.type === z && (H = I % i.numberSectionStyles);
      let V = "";
      return h.active ? h.crit ? V += " activeCrit" : V = " active" : h.done ? h.crit ? V = " doneCrit" : V = " done" : h.crit && (V += " crit"), V.length === 0 && (V = " task"), h.milestone && (V = " milestone " + V), V += H, V += " " + G, U + V;
    }), c.append("text").attr("id", function(h) {
      return h.id + "-text";
    }).text(function(h) {
      return h.task;
    }).attr("font-size", i.fontSize).attr("x", function(h) {
      let U = g(h.startTime), G = g(h.renderEndTime || h.endTime);
      h.milestone && (U += 0.5 * (g(h.endTime) - g(h.startTime)) - 0.5 * o), h.milestone && (G = U + o);
      const H = this.getBBox().width;
      return H > G - U ? G + H + 1.5 * i.leftPadding > m ? U + v - 5 : G + v + 5 : (G - U) / 2 + U + v;
    }).attr("y", function(h, U) {
      return U = h.order, U * Y + i.barHeight / 2 + (i.fontSize / 2 - 2) + D;
    }).attr("text-height", o).attr("class", function(h) {
      const U = g(h.startTime);
      let G = g(h.endTime);
      h.milestone && (G = U + o);
      const H = this.getBBox().width;
      let V = "";
      h.classes.length > 0 && (V = h.classes.join(" "));
      let I = 0;
      for (const [st, it] of F.entries())
        h.type === it && (I = st % i.numberSectionStyles);
      let z = "";
      return h.active && (h.crit ? z = "activeCritText" + I : z = "activeText" + I), h.done ? h.crit ? z = z + " doneCritText" + I : z = z + " doneText" + I : h.crit && (z = z + " critText" + I), h.milestone && (z += " milestoneText"), H > G - U ? G + H + 1.5 * i.leftPadding > m ? V + " taskTextOutsideLeft taskTextOutside" + I + " " + z : V + " taskTextOutsideRight taskTextOutside" + I + " " + z + " width-" + H : V + " taskText taskText" + I + " " + z + " width-" + H;
    }), xt().securityLevel === "sandbox") {
      let h;
      h = Pt("#i" + e);
      const U = h.nodes()[0].contentDocument;
      c.filter(function(G) {
        return X[G.id] !== void 0;
      }).each(function(G) {
        var H = U.querySelector("#" + G.id), V = U.querySelector("#" + G.id + "-text");
        const I = H.parentNode;
        var z = U.createElement("a");
        z.setAttribute("xlink:href", X[G.id]), z.setAttribute("target", "_top"), I.appendChild(z), z.appendChild(H), z.appendChild(V);
      });
    }
  }
  function B(T, Y, D, v, o, d, m, u) {
    if (m.length === 0 && u.length === 0)
      return;
    let _, c;
    for (const { startTime: H, endTime: V } of d)
      (_ === void 0 || H < _) && (_ = H), (c === void 0 || V > c) && (c = V);
    if (!_ || !c)
      return;
    if (nt(c).diff(nt(_), "year") > 5) {
      qt.warn(
        "The difference between the min and max time is more than 5 years. This will cause performance issues. Skipping drawing exclude days."
      );
      return;
    }
    const X = r.db.getDateFormat(), f = [];
    let h = null, U = nt(_);
    for (; U.valueOf() <= c; )
      r.db.isInvalidDate(U, X, m, u) ? h ? h.end = U : h = {
        start: U,
        end: U
      } : h && (f.push(h), h = null), U = U.add(1, "d");
    q.append("g").selectAll("rect").data(f).enter().append("rect").attr("id", function(H) {
      return "exclude-" + H.start.format("YYYY-MM-DD");
    }).attr("x", function(H) {
      return g(H.start) + D;
    }).attr("y", i.gridLineStartPadding).attr("width", function(H) {
      const V = H.end.add(1, "day");
      return g(V) - g(H.start);
    }).attr("height", o - Y - i.gridLineStartPadding).attr("transform-origin", function(H, V) {
      return (g(H.start) + D + 0.5 * (g(H.end) - g(H.start))).toString() + "px " + (V * T + 0.5 * o).toString() + "px";
    }).attr("class", "exclude-range");
  }
  function Z(T, Y, D, v) {
    let o = Kn(g).tickSize(-v + Y + i.gridLineStartPadding).tickFormat(Qt(r.db.getAxisFormat() || i.axisFormat || "%Y-%m-%d"));
    const m = /^([1-9]\d*)(millisecond|second|minute|hour|day|week|month)$/.exec(
      r.db.getTickInterval() || i.tickInterval
    );
    if (m !== null) {
      const u = m[1], _ = m[2], c = r.db.getWeekday() || i.weekday;
      switch (_) {
        case "millisecond":
          o.ticks(Dt.every(u));
          break;
        case "second":
          o.ticks(gt.every(u));
          break;
        case "minute":
          o.ticks(Et.every(u));
          break;
        case "hour":
          o.ticks(At.every(u));
          break;
        case "day":
          o.ticks(yt.every(u));
          break;
        case "week":
          o.ticks(Re[c].every(u));
          break;
        case "month":
          o.ticks(Wt.every(u));
          break;
      }
    }
    if (q.append("g").attr("class", "grid").attr("transform", "translate(" + T + ", " + (v - 50) + ")").call(o).selectAll("text").style("text-anchor", "middle").attr("fill", "#000").attr("stroke", "none").attr("font-size", 10).attr("dy", "1em"), r.db.topAxisEnabled() || i.topAxis) {
      let u = Jn(g).tickSize(-v + Y + i.gridLineStartPadding).tickFormat(Qt(r.db.getAxisFormat() || i.axisFormat || "%Y-%m-%d"));
      if (m !== null) {
        const _ = m[1], c = m[2], X = r.db.getWeekday() || i.weekday;
        switch (c) {
          case "millisecond":
            u.ticks(Dt.every(_));
            break;
          case "second":
            u.ticks(gt.every(_));
            break;
          case "minute":
            u.ticks(Et.every(_));
            break;
          case "hour":
            u.ticks(At.every(_));
            break;
          case "day":
            u.ticks(yt.every(_));
            break;
          case "week":
            u.ticks(Re[X].every(_));
            break;
          case "month":
            u.ticks(Wt.every(_));
            break;
        }
      }
      q.append("g").attr("class", "grid").attr("transform", "translate(" + T + ", " + Y + ")").call(u).selectAll("text").style("text-anchor", "middle").attr("fill", "#000").attr("stroke", "none").attr("font-size", 10);
    }
  }
  function Q(T, Y) {
    let D = 0;
    const v = Object.keys(w).map((o) => [o, w[o]]);
    q.append("g").selectAll("text").data(v).enter().append(function(o) {
      const d = o[0].split(On.lineBreakRegex), m = -(d.length - 1) / 2, u = S.createElementNS("http://www.w3.org/2000/svg", "text");
      u.setAttribute("dy", m + "em");
      for (const [_, c] of d.entries()) {
        const X = S.createElementNS("http://www.w3.org/2000/svg", "tspan");
        X.setAttribute("alignment-baseline", "central"), X.setAttribute("x", "10"), _ > 0 && X.setAttribute("dy", "1em"), X.textContent = c, u.appendChild(X);
      }
      return u;
    }).attr("x", 10).attr("y", function(o, d) {
      if (d > 0)
        for (let m = 0; m < d; m++)
          return D += v[d - 1][1], o[1] * T / 2 + D * T + Y;
      else
        return o[1] * T / 2 + Y;
    }).attr("font-size", i.sectionFontSize).attr("class", function(o) {
      for (const [d, m] of F.entries())
        if (o[0] === m)
          return "sectionTitle sectionTitle" + d % i.numberSectionStyles;
      return "sectionTitle";
    });
  }
  function b(T, Y, D, v) {
    const o = r.db.getTodayMarker();
    if (o === "off")
      return;
    const d = q.append("g").attr("class", "today"), m = /* @__PURE__ */ new Date(), u = d.append("line");
    u.attr("x1", g(m) + T).attr("x2", g(m) + T).attr("y1", i.titleTopMargin).attr("y2", v - i.titleTopMargin).attr("class", "today"), o !== "" && u.attr("style", o.replace(/,/g, ";"));
  }
  function A(T) {
    const Y = {}, D = [];
    for (let v = 0, o = T.length; v < o; ++v)
      Object.prototype.hasOwnProperty.call(Y, T[v]) || (Y[T[v]] = !0, D.push(T[v]));
    return D;
  }
}, ds = {
  setConf: us,
  draw: hs
}, ms = (t) => `
  .mermaid-main-font {
    font-family: var(--mermaid-font-family, "trebuchet ms", verdana, arial, sans-serif);
  }

  .exclude-range {
    fill: ${t.excludeBkgColor};
  }

  .section {
    stroke: none;
    opacity: 0.2;
  }

  .section0 {
    fill: ${t.sectionBkgColor};
  }

  .section2 {
    fill: ${t.sectionBkgColor2};
  }

  .section1,
  .section3 {
    fill: ${t.altSectionBkgColor};
    opacity: 0.2;
  }

  .sectionTitle0 {
    fill: ${t.titleColor};
  }

  .sectionTitle1 {
    fill: ${t.titleColor};
  }

  .sectionTitle2 {
    fill: ${t.titleColor};
  }

  .sectionTitle3 {
    fill: ${t.titleColor};
  }

  .sectionTitle {
    text-anchor: start;
    font-family: var(--mermaid-font-family, "trebuchet ms", verdana, arial, sans-serif);
  }


  /* Grid and axis */

  .grid .tick {
    stroke: ${t.gridColor};
    opacity: 0.8;
    shape-rendering: crispEdges;
  }

  .grid .tick text {
    font-family: ${t.fontFamily};
    fill: ${t.textColor};
  }

  .grid path {
    stroke-width: 0;
  }


  /* Today line */

  .today {
    fill: none;
    stroke: ${t.todayLineColor};
    stroke-width: 2px;
  }


  /* Task styling */

  /* Default task */

  .task {
    stroke-width: 2;
  }

  .taskText {
    text-anchor: middle;
    font-family: var(--mermaid-font-family, "trebuchet ms", verdana, arial, sans-serif);
  }

  .taskTextOutsideRight {
    fill: ${t.taskTextDarkColor};
    text-anchor: start;
    font-family: var(--mermaid-font-family, "trebuchet ms", verdana, arial, sans-serif);
  }

  .taskTextOutsideLeft {
    fill: ${t.taskTextDarkColor};
    text-anchor: end;
  }


  /* Special case clickable */

  .task.clickable {
    cursor: pointer;
  }

  .taskText.clickable {
    cursor: pointer;
    fill: ${t.taskTextClickableColor} !important;
    font-weight: bold;
  }

  .taskTextOutsideLeft.clickable {
    cursor: pointer;
    fill: ${t.taskTextClickableColor} !important;
    font-weight: bold;
  }

  .taskTextOutsideRight.clickable {
    cursor: pointer;
    fill: ${t.taskTextClickableColor} !important;
    font-weight: bold;
  }


  /* Specific task settings for the sections*/

  .taskText0,
  .taskText1,
  .taskText2,
  .taskText3 {
    fill: ${t.taskTextColor};
  }

  .task0,
  .task1,
  .task2,
  .task3 {
    fill: ${t.taskBkgColor};
    stroke: ${t.taskBorderColor};
  }

  .taskTextOutside0,
  .taskTextOutside2
  {
    fill: ${t.taskTextOutsideColor};
  }

  .taskTextOutside1,
  .taskTextOutside3 {
    fill: ${t.taskTextOutsideColor};
  }


  /* Active task */

  .active0,
  .active1,
  .active2,
  .active3 {
    fill: ${t.activeTaskBkgColor};
    stroke: ${t.activeTaskBorderColor};
  }

  .activeText0,
  .activeText1,
  .activeText2,
  .activeText3 {
    fill: ${t.taskTextDarkColor} !important;
  }


  /* Completed task */

  .done0,
  .done1,
  .done2,
  .done3 {
    stroke: ${t.doneTaskBorderColor};
    fill: ${t.doneTaskBkgColor};
    stroke-width: 2;
  }

  .doneText0,
  .doneText1,
  .doneText2,
  .doneText3 {
    fill: ${t.taskTextDarkColor} !important;
  }


  /* Tasks on the critical line */

  .crit0,
  .crit1,
  .crit2,
  .crit3 {
    stroke: ${t.critBorderColor};
    fill: ${t.critBkgColor};
    stroke-width: 2;
  }

  .activeCrit0,
  .activeCrit1,
  .activeCrit2,
  .activeCrit3 {
    stroke: ${t.critBorderColor};
    fill: ${t.activeTaskBkgColor};
    stroke-width: 2;
  }

  .doneCrit0,
  .doneCrit1,
  .doneCrit2,
  .doneCrit3 {
    stroke: ${t.critBorderColor};
    fill: ${t.doneTaskBkgColor};
    stroke-width: 2;
    cursor: pointer;
    shape-rendering: crispEdges;
  }

  .milestone {
    transform: rotate(45deg) scale(0.8,0.8);
  }

  .milestoneText {
    font-style: italic;
  }
  .doneCritText0,
  .doneCritText1,
  .doneCritText2,
  .doneCritText3 {
    fill: ${t.taskTextDarkColor} !important;
  }

  .activeCritText0,
  .activeCritText1,
  .activeCritText2,
  .activeCritText3 {
    fill: ${t.taskTextDarkColor} !important;
  }

  .titleText {
    text-anchor: middle;
    font-size: 18px;
    fill: ${t.titleColor || t.textColor};
    font-family: var(--mermaid-font-family, "trebuchet ms", verdana, arial, sans-serif);
  }
`, gs = ms, Ts = {
  parser: xi,
  db: ls,
  renderer: ds,
  styles: gs
};
export {
  Ts as diagram
};
