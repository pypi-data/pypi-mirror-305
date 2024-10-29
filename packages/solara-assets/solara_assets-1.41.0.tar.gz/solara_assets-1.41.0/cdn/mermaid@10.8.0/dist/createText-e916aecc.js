import { b5 as At, l as zt, b4 as It } from "./mermaid-a09fe7cd.js";
const Tt = {};
function Bt(n, r) {
  const t = r || Tt, e = typeof t.includeImageAlt == "boolean" ? t.includeImageAlt : !0, u = typeof t.includeHtml == "boolean" ? t.includeHtml : !0;
  return et(n, e, u);
}
function et(n, r, t) {
  if (Lt(n)) {
    if ("value" in n)
      return n.type === "html" && !t ? "" : n.value;
    if (r && "alt" in n && n.alt)
      return n.alt;
    if ("children" in n)
      return Vn(n.children, r, t);
  }
  return Array.isArray(n) ? Vn(n, r, t) : "";
}
function Vn(n, r, t) {
  const e = [];
  let u = -1;
  for (; ++u < n.length; )
    e[u] = et(n[u], r, t);
  return e.join("");
}
function Lt(n) {
  return !!(n && typeof n == "object");
}
function tn(n, r, t, e) {
  const u = n.length;
  let i = 0, l;
  if (r < 0 ? r = -r > u ? 0 : u + r : r = r > u ? u : r, t = t > 0 ? t : 0, e.length < 1e4)
    l = Array.from(e), l.unshift(r, t), n.splice(...l);
  else
    for (t && n.splice(r, t); i < e.length; )
      l = e.slice(i, i + 1e4), l.unshift(r, 0), n.splice(...l), i += 1e4, r += 1e4;
}
function Y(n, r) {
  return n.length > 0 ? (tn(n, n.length, 0, r), n) : r;
}
const Wn = {}.hasOwnProperty;
function Ot(n) {
  const r = {};
  let t = -1;
  for (; ++t < n.length; )
    Dt(r, n[t]);
  return r;
}
function Dt(n, r) {
  let t;
  for (t in r) {
    const u = (Wn.call(n, t) ? n[t] : void 0) || (n[t] = {}), i = r[t];
    let l;
    if (i)
      for (l in i) {
        Wn.call(u, l) || (u[l] = []);
        const a = i[l];
        Pt(
          // @ts-expect-error Looks like a list.
          u[l],
          Array.isArray(a) ? a : a ? [a] : []
        );
      }
  }
}
function Pt(n, r) {
  let t = -1;
  const e = [];
  for (; ++t < r.length; )
    (r[t].add === "after" ? n : e).push(r[t]);
  tn(n, 0, 0, e);
}
const _t = /[!-\/:-@\[-`\{-~\xA1\xA7\xAB\xB6\xB7\xBB\xBF\u037E\u0387\u055A-\u055F\u0589\u058A\u05BE\u05C0\u05C3\u05C6\u05F3\u05F4\u0609\u060A\u060C\u060D\u061B\u061D-\u061F\u066A-\u066D\u06D4\u0700-\u070D\u07F7-\u07F9\u0830-\u083E\u085E\u0964\u0965\u0970\u09FD\u0A76\u0AF0\u0C77\u0C84\u0DF4\u0E4F\u0E5A\u0E5B\u0F04-\u0F12\u0F14\u0F3A-\u0F3D\u0F85\u0FD0-\u0FD4\u0FD9\u0FDA\u104A-\u104F\u10FB\u1360-\u1368\u1400\u166E\u169B\u169C\u16EB-\u16ED\u1735\u1736\u17D4-\u17D6\u17D8-\u17DA\u1800-\u180A\u1944\u1945\u1A1E\u1A1F\u1AA0-\u1AA6\u1AA8-\u1AAD\u1B5A-\u1B60\u1B7D\u1B7E\u1BFC-\u1BFF\u1C3B-\u1C3F\u1C7E\u1C7F\u1CC0-\u1CC7\u1CD3\u2010-\u2027\u2030-\u2043\u2045-\u2051\u2053-\u205E\u207D\u207E\u208D\u208E\u2308-\u230B\u2329\u232A\u2768-\u2775\u27C5\u27C6\u27E6-\u27EF\u2983-\u2998\u29D8-\u29DB\u29FC\u29FD\u2CF9-\u2CFC\u2CFE\u2CFF\u2D70\u2E00-\u2E2E\u2E30-\u2E4F\u2E52-\u2E5D\u3001-\u3003\u3008-\u3011\u3014-\u301F\u3030\u303D\u30A0\u30FB\uA4FE\uA4FF\uA60D-\uA60F\uA673\uA67E\uA6F2-\uA6F7\uA874-\uA877\uA8CE\uA8CF\uA8F8-\uA8FA\uA8FC\uA92E\uA92F\uA95F\uA9C1-\uA9CD\uA9DE\uA9DF\uAA5C-\uAA5F\uAADE\uAADF\uAAF0\uAAF1\uABEB\uFD3E\uFD3F\uFE10-\uFE19\uFE30-\uFE52\uFE54-\uFE61\uFE63\uFE68\uFE6A\uFE6B\uFF01-\uFF03\uFF05-\uFF0A\uFF0C-\uFF0F\uFF1A\uFF1B\uFF1F\uFF20\uFF3B-\uFF3D\uFF3F\uFF5B\uFF5D\uFF5F-\uFF65]/, nn = cn(/[A-Za-z]/), v = cn(/[\dA-Za-z]/), Mt = cn(/[#-'*+\--9=?A-Z^-~]/);
function An(n) {
  return (
    // Special whitespace codes (which have negative values), C0 and Control
    // character DEL
    n !== null && (n < 32 || n === 127)
  );
}
const zn = cn(/\d/), jt = cn(/[\dA-Fa-f]/), Rt = cn(/[!-/:-@[-`{-~]/);
function C(n) {
  return n !== null && n < -2;
}
function Z(n) {
  return n !== null && (n < 0 || n === 32);
}
function z(n) {
  return n === -2 || n === -1 || n === 32;
}
const qt = cn(_t), Ht = cn(/\s/);
function cn(n) {
  return r;
  function r(t) {
    return t !== null && n.test(String.fromCharCode(t));
  }
}
function O(n, r, t, e) {
  const u = e ? e - 1 : Number.POSITIVE_INFINITY;
  let i = 0;
  return l;
  function l(m) {
    return z(m) ? (n.enter(t), a(m)) : r(m);
  }
  function a(m) {
    return z(m) && i++ < u ? (n.consume(m), a) : (n.exit(t), r(m));
  }
}
const Nt = {
  tokenize: Vt
};
function Vt(n) {
  const r = n.attempt(
    this.parser.constructs.contentInitial,
    e,
    u
  );
  let t;
  return r;
  function e(a) {
    if (a === null) {
      n.consume(a);
      return;
    }
    return n.enter("lineEnding"), n.consume(a), n.exit("lineEnding"), O(n, r, "linePrefix");
  }
  function u(a) {
    return n.enter("paragraph"), i(a);
  }
  function i(a) {
    const m = n.enter("chunkText", {
      contentType: "text",
      previous: t
    });
    return t && (t.next = m), t = m, l(a);
  }
  function l(a) {
    if (a === null) {
      n.exit("chunkText"), n.exit("paragraph"), n.consume(a);
      return;
    }
    return C(a) ? (n.consume(a), n.exit("chunkText"), i) : (n.consume(a), l);
  }
}
const Wt = {
  tokenize: Qt
}, Qn = {
  tokenize: Ut
};
function Qt(n) {
  const r = this, t = [];
  let e = 0, u, i, l;
  return a;
  function a(F) {
    if (e < t.length) {
      const D = t[e];
      return r.containerState = D[1], n.attempt(
        D[0].continuation,
        m,
        c
      )(F);
    }
    return c(F);
  }
  function m(F) {
    if (e++, r.containerState._closeFlow) {
      r.containerState._closeFlow = void 0, u && j();
      const D = r.events.length;
      let _ = D, k;
      for (; _--; )
        if (r.events[_][0] === "exit" && r.events[_][1].type === "chunkFlow") {
          k = r.events[_][1].end;
          break;
        }
      b(e);
      let T = D;
      for (; T < r.events.length; )
        r.events[T][1].end = Object.assign({}, k), T++;
      return tn(
        r.events,
        _ + 1,
        0,
        r.events.slice(D)
      ), r.events.length = T, c(F);
    }
    return a(F);
  }
  function c(F) {
    if (e === t.length) {
      if (!u)
        return x(F);
      if (u.currentConstruct && u.currentConstruct.concrete)
        return A(F);
      r.interrupt = !!(u.currentConstruct && !u._gfmTableDynamicInterruptHack);
    }
    return r.containerState = {}, n.check(
      Qn,
      p,
      f
    )(F);
  }
  function p(F) {
    return u && j(), b(e), x(F);
  }
  function f(F) {
    return r.parser.lazy[r.now().line] = e !== t.length, l = r.now().offset, A(F);
  }
  function x(F) {
    return r.containerState = {}, n.attempt(
      Qn,
      h,
      A
    )(F);
  }
  function h(F) {
    return e++, t.push([r.currentConstruct, r.containerState]), x(F);
  }
  function A(F) {
    if (F === null) {
      u && j(), b(0), n.consume(F);
      return;
    }
    return u = u || r.parser.flow(r.now()), n.enter("chunkFlow", {
      contentType: "flow",
      previous: i,
      _tokenizer: u
    }), I(F);
  }
  function I(F) {
    if (F === null) {
      M(n.exit("chunkFlow"), !0), b(0), n.consume(F);
      return;
    }
    return C(F) ? (n.consume(F), M(n.exit("chunkFlow")), e = 0, r.interrupt = void 0, a) : (n.consume(F), I);
  }
  function M(F, D) {
    const _ = r.sliceStream(F);
    if (D && _.push(null), F.previous = i, i && (i.next = F), i = F, u.defineSkip(F.start), u.write(_), r.parser.lazy[F.start.line]) {
      let k = u.events.length;
      for (; k--; )
        if (
          // The token starts before the line ending…
          u.events[k][1].start.offset < l && // …and either is not ended yet…
          (!u.events[k][1].end || // …or ends after it.
          u.events[k][1].end.offset > l)
        )
          return;
      const T = r.events.length;
      let H = T, N, V;
      for (; H--; )
        if (r.events[H][0] === "exit" && r.events[H][1].type === "chunkFlow") {
          if (N) {
            V = r.events[H][1].end;
            break;
          }
          N = !0;
        }
      for (b(e), k = T; k < r.events.length; )
        r.events[k][1].end = Object.assign({}, V), k++;
      tn(
        r.events,
        H + 1,
        0,
        r.events.slice(T)
      ), r.events.length = k;
    }
  }
  function b(F) {
    let D = t.length;
    for (; D-- > F; ) {
      const _ = t[D];
      r.containerState = _[1], _[0].exit.call(r, n);
    }
    t.length = F;
  }
  function j() {
    u.write([null]), i = void 0, u = void 0, r.containerState._closeFlow = void 0;
  }
}
function Ut(n, r, t) {
  return O(
    n,
    n.attempt(this.parser.constructs.document, r, t),
    "linePrefix",
    this.parser.constructs.disable.null.includes("codeIndented") ? void 0 : 4
  );
}
function Un(n) {
  if (n === null || Z(n) || Ht(n))
    return 1;
  if (qt(n))
    return 2;
}
function Ln(n, r, t) {
  const e = [];
  let u = -1;
  for (; ++u < n.length; ) {
    const i = n[u].resolveAll;
    i && !e.includes(i) && (r = i(r, t), e.push(i));
  }
  return r;
}
const In = {
  name: "attention",
  tokenize: Zt,
  resolveAll: $t
};
function $t(n, r) {
  let t = -1, e, u, i, l, a, m, c, p;
  for (; ++t < n.length; )
    if (n[t][0] === "enter" && n[t][1].type === "attentionSequence" && n[t][1]._close) {
      for (e = t; e--; )
        if (n[e][0] === "exit" && n[e][1].type === "attentionSequence" && n[e][1]._open && // If the markers are the same:
        r.sliceSerialize(n[e][1]).charCodeAt(0) === r.sliceSerialize(n[t][1]).charCodeAt(0)) {
          if ((n[e][1]._close || n[t][1]._open) && (n[t][1].end.offset - n[t][1].start.offset) % 3 && !((n[e][1].end.offset - n[e][1].start.offset + n[t][1].end.offset - n[t][1].start.offset) % 3))
            continue;
          m = n[e][1].end.offset - n[e][1].start.offset > 1 && n[t][1].end.offset - n[t][1].start.offset > 1 ? 2 : 1;
          const f = Object.assign({}, n[e][1].end), x = Object.assign({}, n[t][1].start);
          $n(f, -m), $n(x, m), l = {
            type: m > 1 ? "strongSequence" : "emphasisSequence",
            start: f,
            end: Object.assign({}, n[e][1].end)
          }, a = {
            type: m > 1 ? "strongSequence" : "emphasisSequence",
            start: Object.assign({}, n[t][1].start),
            end: x
          }, i = {
            type: m > 1 ? "strongText" : "emphasisText",
            start: Object.assign({}, n[e][1].end),
            end: Object.assign({}, n[t][1].start)
          }, u = {
            type: m > 1 ? "strong" : "emphasis",
            start: Object.assign({}, l.start),
            end: Object.assign({}, a.end)
          }, n[e][1].end = Object.assign({}, l.start), n[t][1].start = Object.assign({}, a.end), c = [], n[e][1].end.offset - n[e][1].start.offset && (c = Y(c, [
            ["enter", n[e][1], r],
            ["exit", n[e][1], r]
          ])), c = Y(c, [
            ["enter", u, r],
            ["enter", l, r],
            ["exit", l, r],
            ["enter", i, r]
          ]), c = Y(
            c,
            Ln(
              r.parser.constructs.insideSpan.null,
              n.slice(e + 1, t),
              r
            )
          ), c = Y(c, [
            ["exit", i, r],
            ["enter", a, r],
            ["exit", a, r],
            ["exit", u, r]
          ]), n[t][1].end.offset - n[t][1].start.offset ? (p = 2, c = Y(c, [
            ["enter", n[t][1], r],
            ["exit", n[t][1], r]
          ])) : p = 0, tn(n, e - 1, t - e + 3, c), t = e + c.length - p - 2;
          break;
        }
    }
  for (t = -1; ++t < n.length; )
    n[t][1].type === "attentionSequence" && (n[t][1].type = "data");
  return n;
}
function Zt(n, r) {
  const t = this.parser.constructs.attentionMarkers.null, e = this.previous, u = Un(e);
  let i;
  return l;
  function l(m) {
    return i = m, n.enter("attentionSequence"), a(m);
  }
  function a(m) {
    if (m === i)
      return n.consume(m), a;
    const c = n.exit("attentionSequence"), p = Un(m), f = !p || p === 2 && u || t.includes(m), x = !u || u === 2 && p || t.includes(e);
    return c._open = !!(i === 42 ? f : f && (u || !x)), c._close = !!(i === 42 ? x : x && (p || !f)), r(m);
  }
}
function $n(n, r) {
  n.column += r, n.offset += r, n._bufferIndex += r;
}
const Yt = {
  name: "autolink",
  tokenize: Gt
};
function Gt(n, r, t) {
  let e = 0;
  return u;
  function u(h) {
    return n.enter("autolink"), n.enter("autolinkMarker"), n.consume(h), n.exit("autolinkMarker"), n.enter("autolinkProtocol"), i;
  }
  function i(h) {
    return nn(h) ? (n.consume(h), l) : c(h);
  }
  function l(h) {
    return h === 43 || h === 45 || h === 46 || v(h) ? (e = 1, a(h)) : c(h);
  }
  function a(h) {
    return h === 58 ? (n.consume(h), e = 0, m) : (h === 43 || h === 45 || h === 46 || v(h)) && e++ < 32 ? (n.consume(h), a) : (e = 0, c(h));
  }
  function m(h) {
    return h === 62 ? (n.exit("autolinkProtocol"), n.enter("autolinkMarker"), n.consume(h), n.exit("autolinkMarker"), n.exit("autolink"), r) : h === null || h === 32 || h === 60 || An(h) ? t(h) : (n.consume(h), m);
  }
  function c(h) {
    return h === 64 ? (n.consume(h), p) : Mt(h) ? (n.consume(h), c) : t(h);
  }
  function p(h) {
    return v(h) ? f(h) : t(h);
  }
  function f(h) {
    return h === 46 ? (n.consume(h), e = 0, p) : h === 62 ? (n.exit("autolinkProtocol").type = "autolinkEmail", n.enter("autolinkMarker"), n.consume(h), n.exit("autolinkMarker"), n.exit("autolink"), r) : x(h);
  }
  function x(h) {
    if ((h === 45 || v(h)) && e++ < 63) {
      const A = h === 45 ? x : f;
      return n.consume(h), A;
    }
    return t(h);
  }
}
const Sn = {
  tokenize: Jt,
  partial: !0
};
function Jt(n, r, t) {
  return e;
  function e(i) {
    return z(i) ? O(n, u, "linePrefix")(i) : u(i);
  }
  function u(i) {
    return i === null || C(i) ? r(i) : t(i);
  }
}
const rt = {
  name: "blockQuote",
  tokenize: Kt,
  continuation: {
    tokenize: Xt
  },
  exit: vt
};
function Kt(n, r, t) {
  const e = this;
  return u;
  function u(l) {
    if (l === 62) {
      const a = e.containerState;
      return a.open || (n.enter("blockQuote", {
        _container: !0
      }), a.open = !0), n.enter("blockQuotePrefix"), n.enter("blockQuoteMarker"), n.consume(l), n.exit("blockQuoteMarker"), i;
    }
    return t(l);
  }
  function i(l) {
    return z(l) ? (n.enter("blockQuotePrefixWhitespace"), n.consume(l), n.exit("blockQuotePrefixWhitespace"), n.exit("blockQuotePrefix"), r) : (n.exit("blockQuotePrefix"), r(l));
  }
}
function Xt(n, r, t) {
  const e = this;
  return u;
  function u(l) {
    return z(l) ? O(
      n,
      i,
      "linePrefix",
      e.parser.constructs.disable.null.includes("codeIndented") ? void 0 : 4
    )(l) : i(l);
  }
  function i(l) {
    return n.attempt(rt, r, t)(l);
  }
}
function vt(n) {
  n.exit("blockQuote");
}
const it = {
  name: "characterEscape",
  tokenize: ne
};
function ne(n, r, t) {
  return e;
  function e(i) {
    return n.enter("characterEscape"), n.enter("escapeMarker"), n.consume(i), n.exit("escapeMarker"), u;
  }
  function u(i) {
    return Rt(i) ? (n.enter("characterEscapeValue"), n.consume(i), n.exit("characterEscapeValue"), n.exit("characterEscape"), r) : t(i);
  }
}
const Zn = document.createElement("i");
function On(n) {
  const r = "&" + n + ";";
  Zn.innerHTML = r;
  const t = Zn.textContent;
  return t.charCodeAt(t.length - 1) === 59 && n !== "semi" || t === r ? !1 : t;
}
const ut = {
  name: "characterReference",
  tokenize: te
};
function te(n, r, t) {
  const e = this;
  let u = 0, i, l;
  return a;
  function a(f) {
    return n.enter("characterReference"), n.enter("characterReferenceMarker"), n.consume(f), n.exit("characterReferenceMarker"), m;
  }
  function m(f) {
    return f === 35 ? (n.enter("characterReferenceMarkerNumeric"), n.consume(f), n.exit("characterReferenceMarkerNumeric"), c) : (n.enter("characterReferenceValue"), i = 31, l = v, p(f));
  }
  function c(f) {
    return f === 88 || f === 120 ? (n.enter("characterReferenceMarkerHexadecimal"), n.consume(f), n.exit("characterReferenceMarkerHexadecimal"), n.enter("characterReferenceValue"), i = 6, l = jt, p) : (n.enter("characterReferenceValue"), i = 7, l = zn, p(f));
  }
  function p(f) {
    if (f === 59 && u) {
      const x = n.exit("characterReferenceValue");
      return l === v && !On(e.sliceSerialize(x)) ? t(f) : (n.enter("characterReferenceMarker"), n.consume(f), n.exit("characterReferenceMarker"), n.exit("characterReference"), r);
    }
    return l(f) && u++ < i ? (n.consume(f), p) : t(f);
  }
}
const Yn = {
  tokenize: re,
  partial: !0
}, Gn = {
  name: "codeFenced",
  tokenize: ee,
  concrete: !0
};
function ee(n, r, t) {
  const e = this, u = {
    tokenize: _,
    partial: !0
  };
  let i = 0, l = 0, a;
  return m;
  function m(k) {
    return c(k);
  }
  function c(k) {
    const T = e.events[e.events.length - 1];
    return i = T && T[1].type === "linePrefix" ? T[2].sliceSerialize(T[1], !0).length : 0, a = k, n.enter("codeFenced"), n.enter("codeFencedFence"), n.enter("codeFencedFenceSequence"), p(k);
  }
  function p(k) {
    return k === a ? (l++, n.consume(k), p) : l < 3 ? t(k) : (n.exit("codeFencedFenceSequence"), z(k) ? O(n, f, "whitespace")(k) : f(k));
  }
  function f(k) {
    return k === null || C(k) ? (n.exit("codeFencedFence"), e.interrupt ? r(k) : n.check(Yn, I, D)(k)) : (n.enter("codeFencedFenceInfo"), n.enter("chunkString", {
      contentType: "string"
    }), x(k));
  }
  function x(k) {
    return k === null || C(k) ? (n.exit("chunkString"), n.exit("codeFencedFenceInfo"), f(k)) : z(k) ? (n.exit("chunkString"), n.exit("codeFencedFenceInfo"), O(n, h, "whitespace")(k)) : k === 96 && k === a ? t(k) : (n.consume(k), x);
  }
  function h(k) {
    return k === null || C(k) ? f(k) : (n.enter("codeFencedFenceMeta"), n.enter("chunkString", {
      contentType: "string"
    }), A(k));
  }
  function A(k) {
    return k === null || C(k) ? (n.exit("chunkString"), n.exit("codeFencedFenceMeta"), f(k)) : k === 96 && k === a ? t(k) : (n.consume(k), A);
  }
  function I(k) {
    return n.attempt(u, D, M)(k);
  }
  function M(k) {
    return n.enter("lineEnding"), n.consume(k), n.exit("lineEnding"), b;
  }
  function b(k) {
    return i > 0 && z(k) ? O(
      n,
      j,
      "linePrefix",
      i + 1
    )(k) : j(k);
  }
  function j(k) {
    return k === null || C(k) ? n.check(Yn, I, D)(k) : (n.enter("codeFlowValue"), F(k));
  }
  function F(k) {
    return k === null || C(k) ? (n.exit("codeFlowValue"), j(k)) : (n.consume(k), F);
  }
  function D(k) {
    return n.exit("codeFenced"), r(k);
  }
  function _(k, T, H) {
    let N = 0;
    return V;
    function V(w) {
      return k.enter("lineEnding"), k.consume(w), k.exit("lineEnding"), y;
    }
    function y(w) {
      return k.enter("codeFencedFence"), z(w) ? O(
        k,
        S,
        "linePrefix",
        e.parser.constructs.disable.null.includes("codeIndented") ? void 0 : 4
      )(w) : S(w);
    }
    function S(w) {
      return w === a ? (k.enter("codeFencedFenceSequence"), P(w)) : H(w);
    }
    function P(w) {
      return w === a ? (N++, k.consume(w), P) : N >= l ? (k.exit("codeFencedFenceSequence"), z(w) ? O(k, R, "whitespace")(w) : R(w)) : H(w);
    }
    function R(w) {
      return w === null || C(w) ? (k.exit("codeFencedFence"), T(w)) : H(w);
    }
  }
}
function re(n, r, t) {
  const e = this;
  return u;
  function u(l) {
    return l === null ? t(l) : (n.enter("lineEnding"), n.consume(l), n.exit("lineEnding"), i);
  }
  function i(l) {
    return e.parser.lazy[e.now().line] ? t(l) : r(l);
  }
}
const Cn = {
  name: "codeIndented",
  tokenize: ue
}, ie = {
  tokenize: le,
  partial: !0
};
function ue(n, r, t) {
  const e = this;
  return u;
  function u(c) {
    return n.enter("codeIndented"), O(n, i, "linePrefix", 4 + 1)(c);
  }
  function i(c) {
    const p = e.events[e.events.length - 1];
    return p && p[1].type === "linePrefix" && p[2].sliceSerialize(p[1], !0).length >= 4 ? l(c) : t(c);
  }
  function l(c) {
    return c === null ? m(c) : C(c) ? n.attempt(ie, l, m)(c) : (n.enter("codeFlowValue"), a(c));
  }
  function a(c) {
    return c === null || C(c) ? (n.exit("codeFlowValue"), l(c)) : (n.consume(c), a);
  }
  function m(c) {
    return n.exit("codeIndented"), r(c);
  }
}
function le(n, r, t) {
  const e = this;
  return u;
  function u(l) {
    return e.parser.lazy[e.now().line] ? t(l) : C(l) ? (n.enter("lineEnding"), n.consume(l), n.exit("lineEnding"), u) : O(n, i, "linePrefix", 4 + 1)(l);
  }
  function i(l) {
    const a = e.events[e.events.length - 1];
    return a && a[1].type === "linePrefix" && a[2].sliceSerialize(a[1], !0).length >= 4 ? r(l) : C(l) ? u(l) : t(l);
  }
}
const ae = {
  name: "codeText",
  tokenize: ce,
  resolve: oe,
  previous: se
};
function oe(n) {
  let r = n.length - 4, t = 3, e, u;
  if ((n[t][1].type === "lineEnding" || n[t][1].type === "space") && (n[r][1].type === "lineEnding" || n[r][1].type === "space")) {
    for (e = t; ++e < r; )
      if (n[e][1].type === "codeTextData") {
        n[t][1].type = "codeTextPadding", n[r][1].type = "codeTextPadding", t += 2, r -= 2;
        break;
      }
  }
  for (e = t - 1, r++; ++e <= r; )
    u === void 0 ? e !== r && n[e][1].type !== "lineEnding" && (u = e) : (e === r || n[e][1].type === "lineEnding") && (n[u][1].type = "codeTextData", e !== u + 2 && (n[u][1].end = n[e - 1][1].end, n.splice(u + 2, e - u - 2), r -= e - u - 2, e = u + 2), u = void 0);
  return n;
}
function se(n) {
  return n !== 96 || this.events[this.events.length - 1][1].type === "characterEscape";
}
function ce(n, r, t) {
  let e = 0, u, i;
  return l;
  function l(f) {
    return n.enter("codeText"), n.enter("codeTextSequence"), a(f);
  }
  function a(f) {
    return f === 96 ? (n.consume(f), e++, a) : (n.exit("codeTextSequence"), m(f));
  }
  function m(f) {
    return f === null ? t(f) : f === 32 ? (n.enter("space"), n.consume(f), n.exit("space"), m) : f === 96 ? (i = n.enter("codeTextSequence"), u = 0, p(f)) : C(f) ? (n.enter("lineEnding"), n.consume(f), n.exit("lineEnding"), m) : (n.enter("codeTextData"), c(f));
  }
  function c(f) {
    return f === null || f === 32 || f === 96 || C(f) ? (n.exit("codeTextData"), m(f)) : (n.consume(f), c);
  }
  function p(f) {
    return f === 96 ? (n.consume(f), u++, p) : u === e ? (n.exit("codeTextSequence"), n.exit("codeText"), r(f)) : (i.type = "codeTextData", c(f));
  }
}
function lt(n) {
  const r = {};
  let t = -1, e, u, i, l, a, m, c;
  for (; ++t < n.length; ) {
    for (; t in r; )
      t = r[t];
    if (e = n[t], t && e[1].type === "chunkFlow" && n[t - 1][1].type === "listItemPrefix" && (m = e[1]._tokenizer.events, i = 0, i < m.length && m[i][1].type === "lineEndingBlank" && (i += 2), i < m.length && m[i][1].type === "content"))
      for (; ++i < m.length && m[i][1].type !== "content"; )
        m[i][1].type === "chunkText" && (m[i][1]._isInFirstContentOfListItem = !0, i++);
    if (e[0] === "enter")
      e[1].contentType && (Object.assign(r, he(n, t)), t = r[t], c = !0);
    else if (e[1]._container) {
      for (i = t, u = void 0; i-- && (l = n[i], l[1].type === "lineEnding" || l[1].type === "lineEndingBlank"); )
        l[0] === "enter" && (u && (n[u][1].type = "lineEndingBlank"), l[1].type = "lineEnding", u = i);
      u && (e[1].end = Object.assign({}, n[u][1].start), a = n.slice(u, t), a.unshift(e), tn(n, u, t - u + 1, a));
    }
  }
  return !c;
}
function he(n, r) {
  const t = n[r][1], e = n[r][2];
  let u = r - 1;
  const i = [], l = t._tokenizer || e.parser[t.contentType](t.start), a = l.events, m = [], c = {};
  let p, f, x = -1, h = t, A = 0, I = 0;
  const M = [I];
  for (; h; ) {
    for (; n[++u][1] !== h; )
      ;
    i.push(u), h._tokenizer || (p = e.sliceStream(h), h.next || p.push(null), f && l.defineSkip(h.start), h._isInFirstContentOfListItem && (l._gfmTasklistFirstContentOfListItem = !0), l.write(p), h._isInFirstContentOfListItem && (l._gfmTasklistFirstContentOfListItem = void 0)), f = h, h = h.next;
  }
  for (h = t; ++x < a.length; )
    // Find a void token that includes a break.
    a[x][0] === "exit" && a[x - 1][0] === "enter" && a[x][1].type === a[x - 1][1].type && a[x][1].start.line !== a[x][1].end.line && (I = x + 1, M.push(I), h._tokenizer = void 0, h.previous = void 0, h = h.next);
  for (l.events = [], h ? (h._tokenizer = void 0, h.previous = void 0) : M.pop(), x = M.length; x--; ) {
    const b = a.slice(M[x], M[x + 1]), j = i.pop();
    m.unshift([j, j + b.length - 1]), tn(n, j, 2, b);
  }
  for (x = -1; ++x < m.length; )
    c[A + m[x][0]] = A + m[x][1], A += m[x][1] - m[x][0] - 1;
  return c;
}
const pe = {
  tokenize: xe,
  resolve: me
}, fe = {
  tokenize: ge,
  partial: !0
};
function me(n) {
  return lt(n), n;
}
function xe(n, r) {
  let t;
  return e;
  function e(a) {
    return n.enter("content"), t = n.enter("chunkContent", {
      contentType: "content"
    }), u(a);
  }
  function u(a) {
    return a === null ? i(a) : C(a) ? n.check(
      fe,
      l,
      i
    )(a) : (n.consume(a), u);
  }
  function i(a) {
    return n.exit("chunkContent"), n.exit("content"), r(a);
  }
  function l(a) {
    return n.consume(a), n.exit("chunkContent"), t.next = n.enter("chunkContent", {
      contentType: "content",
      previous: t
    }), t = t.next, u;
  }
}
function ge(n, r, t) {
  const e = this;
  return u;
  function u(l) {
    return n.exit("chunkContent"), n.enter("lineEnding"), n.consume(l), n.exit("lineEnding"), O(n, i, "linePrefix");
  }
  function i(l) {
    if (l === null || C(l))
      return t(l);
    const a = e.events[e.events.length - 1];
    return !e.parser.constructs.disable.null.includes("codeIndented") && a && a[1].type === "linePrefix" && a[2].sliceSerialize(a[1], !0).length >= 4 ? r(l) : n.interrupt(e.parser.constructs.flow, t, r)(l);
  }
}
function at(n, r, t, e, u, i, l, a, m) {
  const c = m || Number.POSITIVE_INFINITY;
  let p = 0;
  return f;
  function f(b) {
    return b === 60 ? (n.enter(e), n.enter(u), n.enter(i), n.consume(b), n.exit(i), x) : b === null || b === 32 || b === 41 || An(b) ? t(b) : (n.enter(e), n.enter(l), n.enter(a), n.enter("chunkString", {
      contentType: "string"
    }), I(b));
  }
  function x(b) {
    return b === 62 ? (n.enter(i), n.consume(b), n.exit(i), n.exit(u), n.exit(e), r) : (n.enter(a), n.enter("chunkString", {
      contentType: "string"
    }), h(b));
  }
  function h(b) {
    return b === 62 ? (n.exit("chunkString"), n.exit(a), x(b)) : b === null || b === 60 || C(b) ? t(b) : (n.consume(b), b === 92 ? A : h);
  }
  function A(b) {
    return b === 60 || b === 62 || b === 92 ? (n.consume(b), h) : h(b);
  }
  function I(b) {
    return !p && (b === null || b === 41 || Z(b)) ? (n.exit("chunkString"), n.exit(a), n.exit(l), n.exit(e), r(b)) : p < c && b === 40 ? (n.consume(b), p++, I) : b === 41 ? (n.consume(b), p--, I) : b === null || b === 32 || b === 40 || An(b) ? t(b) : (n.consume(b), b === 92 ? M : I);
  }
  function M(b) {
    return b === 40 || b === 41 || b === 92 ? (n.consume(b), I) : I(b);
  }
}
function ot(n, r, t, e, u, i) {
  const l = this;
  let a = 0, m;
  return c;
  function c(h) {
    return n.enter(e), n.enter(u), n.consume(h), n.exit(u), n.enter(i), p;
  }
  function p(h) {
    return a > 999 || h === null || h === 91 || h === 93 && !m || // To do: remove in the future once we’ve switched from
    // `micromark-extension-footnote` to `micromark-extension-gfm-footnote`,
    // which doesn’t need this.
    // Hidden footnotes hook.
    /* c8 ignore next 3 */
    h === 94 && !a && "_hiddenFootnoteSupport" in l.parser.constructs ? t(h) : h === 93 ? (n.exit(i), n.enter(u), n.consume(h), n.exit(u), n.exit(e), r) : C(h) ? (n.enter("lineEnding"), n.consume(h), n.exit("lineEnding"), p) : (n.enter("chunkString", {
      contentType: "string"
    }), f(h));
  }
  function f(h) {
    return h === null || h === 91 || h === 93 || C(h) || a++ > 999 ? (n.exit("chunkString"), p(h)) : (n.consume(h), m || (m = !z(h)), h === 92 ? x : f);
  }
  function x(h) {
    return h === 91 || h === 92 || h === 93 ? (n.consume(h), a++, f) : f(h);
  }
}
function st(n, r, t, e, u, i) {
  let l;
  return a;
  function a(x) {
    return x === 34 || x === 39 || x === 40 ? (n.enter(e), n.enter(u), n.consume(x), n.exit(u), l = x === 40 ? 41 : x, m) : t(x);
  }
  function m(x) {
    return x === l ? (n.enter(u), n.consume(x), n.exit(u), n.exit(e), r) : (n.enter(i), c(x));
  }
  function c(x) {
    return x === l ? (n.exit(i), m(l)) : x === null ? t(x) : C(x) ? (n.enter("lineEnding"), n.consume(x), n.exit("lineEnding"), O(n, c, "linePrefix")) : (n.enter("chunkString", {
      contentType: "string"
    }), p(x));
  }
  function p(x) {
    return x === l || x === null || C(x) ? (n.exit("chunkString"), c(x)) : (n.consume(x), x === 92 ? f : p);
  }
  function f(x) {
    return x === l || x === 92 ? (n.consume(x), p) : p(x);
  }
}
function dn(n, r) {
  let t;
  return e;
  function e(u) {
    return C(u) ? (n.enter("lineEnding"), n.consume(u), n.exit("lineEnding"), t = !0, e) : z(u) ? O(
      n,
      e,
      t ? "linePrefix" : "lineSuffix"
    )(u) : r(u);
  }
}
function xn(n) {
  return n.replace(/[\t\n\r ]+/g, " ").replace(/^ | $/g, "").toLowerCase().toUpperCase();
}
const ke = {
  name: "definition",
  tokenize: be
}, de = {
  tokenize: ye,
  partial: !0
};
function be(n, r, t) {
  const e = this;
  let u;
  return i;
  function i(h) {
    return n.enter("definition"), l(h);
  }
  function l(h) {
    return ot.call(
      e,
      n,
      a,
      // Note: we don’t need to reset the way `markdown-rs` does.
      t,
      "definitionLabel",
      "definitionLabelMarker",
      "definitionLabelString"
    )(h);
  }
  function a(h) {
    return u = xn(
      e.sliceSerialize(e.events[e.events.length - 1][1]).slice(1, -1)
    ), h === 58 ? (n.enter("definitionMarker"), n.consume(h), n.exit("definitionMarker"), m) : t(h);
  }
  function m(h) {
    return Z(h) ? dn(n, c)(h) : c(h);
  }
  function c(h) {
    return at(
      n,
      p,
      // Note: we don’t need to reset the way `markdown-rs` does.
      t,
      "definitionDestination",
      "definitionDestinationLiteral",
      "definitionDestinationLiteralMarker",
      "definitionDestinationRaw",
      "definitionDestinationString"
    )(h);
  }
  function p(h) {
    return n.attempt(de, f, f)(h);
  }
  function f(h) {
    return z(h) ? O(n, x, "whitespace")(h) : x(h);
  }
  function x(h) {
    return h === null || C(h) ? (n.exit("definition"), e.parser.defined.push(u), r(h)) : t(h);
  }
}
function ye(n, r, t) {
  return e;
  function e(a) {
    return Z(a) ? dn(n, u)(a) : t(a);
  }
  function u(a) {
    return st(
      n,
      i,
      t,
      "definitionTitle",
      "definitionTitleMarker",
      "definitionTitleString"
    )(a);
  }
  function i(a) {
    return z(a) ? O(n, l, "whitespace")(a) : l(a);
  }
  function l(a) {
    return a === null || C(a) ? r(a) : t(a);
  }
}
const Se = {
  name: "hardBreakEscape",
  tokenize: Fe
};
function Fe(n, r, t) {
  return e;
  function e(i) {
    return n.enter("hardBreakEscape"), n.consume(i), u;
  }
  function u(i) {
    return C(i) ? (n.exit("hardBreakEscape"), r(i)) : t(i);
  }
}
const Ee = {
  name: "headingAtx",
  tokenize: we,
  resolve: Ce
};
function Ce(n, r) {
  let t = n.length - 2, e = 3, u, i;
  return n[e][1].type === "whitespace" && (e += 2), t - 2 > e && n[t][1].type === "whitespace" && (t -= 2), n[t][1].type === "atxHeadingSequence" && (e === t - 1 || t - 4 > e && n[t - 2][1].type === "whitespace") && (t -= e + 1 === t ? 2 : 4), t > e && (u = {
    type: "atxHeadingText",
    start: n[e][1].start,
    end: n[t][1].end
  }, i = {
    type: "chunkText",
    start: n[e][1].start,
    end: n[t][1].end,
    contentType: "text"
  }, tn(n, e, t - e + 1, [
    ["enter", u, r],
    ["enter", i, r],
    ["exit", i, r],
    ["exit", u, r]
  ])), n;
}
function we(n, r, t) {
  let e = 0;
  return u;
  function u(p) {
    return n.enter("atxHeading"), i(p);
  }
  function i(p) {
    return n.enter("atxHeadingSequence"), l(p);
  }
  function l(p) {
    return p === 35 && e++ < 6 ? (n.consume(p), l) : p === null || Z(p) ? (n.exit("atxHeadingSequence"), a(p)) : t(p);
  }
  function a(p) {
    return p === 35 ? (n.enter("atxHeadingSequence"), m(p)) : p === null || C(p) ? (n.exit("atxHeading"), r(p)) : z(p) ? O(n, a, "whitespace")(p) : (n.enter("atxHeadingText"), c(p));
  }
  function m(p) {
    return p === 35 ? (n.consume(p), m) : (n.exit("atxHeadingSequence"), a(p));
  }
  function c(p) {
    return p === null || p === 35 || Z(p) ? (n.exit("atxHeadingText"), a(p)) : (n.consume(p), c);
  }
}
const Ae = [
  "address",
  "article",
  "aside",
  "base",
  "basefont",
  "blockquote",
  "body",
  "caption",
  "center",
  "col",
  "colgroup",
  "dd",
  "details",
  "dialog",
  "dir",
  "div",
  "dl",
  "dt",
  "fieldset",
  "figcaption",
  "figure",
  "footer",
  "form",
  "frame",
  "frameset",
  "h1",
  "h2",
  "h3",
  "h4",
  "h5",
  "h6",
  "head",
  "header",
  "hr",
  "html",
  "iframe",
  "legend",
  "li",
  "link",
  "main",
  "menu",
  "menuitem",
  "nav",
  "noframes",
  "ol",
  "optgroup",
  "option",
  "p",
  "param",
  "search",
  "section",
  "summary",
  "table",
  "tbody",
  "td",
  "tfoot",
  "th",
  "thead",
  "title",
  "tr",
  "track",
  "ul"
], Jn = ["pre", "script", "style", "textarea"], ze = {
  name: "htmlFlow",
  tokenize: Le,
  resolveTo: Be,
  concrete: !0
}, Ie = {
  tokenize: De,
  partial: !0
}, Te = {
  tokenize: Oe,
  partial: !0
};
function Be(n) {
  let r = n.length;
  for (; r-- && !(n[r][0] === "enter" && n[r][1].type === "htmlFlow"); )
    ;
  return r > 1 && n[r - 2][1].type === "linePrefix" && (n[r][1].start = n[r - 2][1].start, n[r + 1][1].start = n[r - 2][1].start, n.splice(r - 2, 2)), n;
}
function Le(n, r, t) {
  const e = this;
  let u, i, l, a, m;
  return c;
  function c(s) {
    return p(s);
  }
  function p(s) {
    return n.enter("htmlFlow"), n.enter("htmlFlowData"), n.consume(s), f;
  }
  function f(s) {
    return s === 33 ? (n.consume(s), x) : s === 47 ? (n.consume(s), i = !0, I) : s === 63 ? (n.consume(s), u = 3, e.interrupt ? r : o) : nn(s) ? (n.consume(s), l = String.fromCharCode(s), M) : t(s);
  }
  function x(s) {
    return s === 45 ? (n.consume(s), u = 2, h) : s === 91 ? (n.consume(s), u = 5, a = 0, A) : nn(s) ? (n.consume(s), u = 4, e.interrupt ? r : o) : t(s);
  }
  function h(s) {
    return s === 45 ? (n.consume(s), e.interrupt ? r : o) : t(s);
  }
  function A(s) {
    const K = "CDATA[";
    return s === K.charCodeAt(a++) ? (n.consume(s), a === K.length ? e.interrupt ? r : S : A) : t(s);
  }
  function I(s) {
    return nn(s) ? (n.consume(s), l = String.fromCharCode(s), M) : t(s);
  }
  function M(s) {
    if (s === null || s === 47 || s === 62 || Z(s)) {
      const K = s === 47, hn = l.toLowerCase();
      return !K && !i && Jn.includes(hn) ? (u = 1, e.interrupt ? r(s) : S(s)) : Ae.includes(l.toLowerCase()) ? (u = 6, K ? (n.consume(s), b) : e.interrupt ? r(s) : S(s)) : (u = 7, e.interrupt && !e.parser.lazy[e.now().line] ? t(s) : i ? j(s) : F(s));
    }
    return s === 45 || v(s) ? (n.consume(s), l += String.fromCharCode(s), M) : t(s);
  }
  function b(s) {
    return s === 62 ? (n.consume(s), e.interrupt ? r : S) : t(s);
  }
  function j(s) {
    return z(s) ? (n.consume(s), j) : V(s);
  }
  function F(s) {
    return s === 47 ? (n.consume(s), V) : s === 58 || s === 95 || nn(s) ? (n.consume(s), D) : z(s) ? (n.consume(s), F) : V(s);
  }
  function D(s) {
    return s === 45 || s === 46 || s === 58 || s === 95 || v(s) ? (n.consume(s), D) : _(s);
  }
  function _(s) {
    return s === 61 ? (n.consume(s), k) : z(s) ? (n.consume(s), _) : F(s);
  }
  function k(s) {
    return s === null || s === 60 || s === 61 || s === 62 || s === 96 ? t(s) : s === 34 || s === 39 ? (n.consume(s), m = s, T) : z(s) ? (n.consume(s), k) : H(s);
  }
  function T(s) {
    return s === m ? (n.consume(s), m = null, N) : s === null || C(s) ? t(s) : (n.consume(s), T);
  }
  function H(s) {
    return s === null || s === 34 || s === 39 || s === 47 || s === 60 || s === 61 || s === 62 || s === 96 || Z(s) ? _(s) : (n.consume(s), H);
  }
  function N(s) {
    return s === 47 || s === 62 || z(s) ? F(s) : t(s);
  }
  function V(s) {
    return s === 62 ? (n.consume(s), y) : t(s);
  }
  function y(s) {
    return s === null || C(s) ? S(s) : z(s) ? (n.consume(s), y) : t(s);
  }
  function S(s) {
    return s === 45 && u === 2 ? (n.consume(s), U) : s === 60 && u === 1 ? (n.consume(s), W) : s === 62 && u === 4 ? (n.consume(s), J) : s === 63 && u === 3 ? (n.consume(s), o) : s === 93 && u === 5 ? (n.consume(s), en) : C(s) && (u === 6 || u === 7) ? (n.exit("htmlFlowData"), n.check(
      Ie,
      rn,
      P
    )(s)) : s === null || C(s) ? (n.exit("htmlFlowData"), P(s)) : (n.consume(s), S);
  }
  function P(s) {
    return n.check(
      Te,
      R,
      rn
    )(s);
  }
  function R(s) {
    return n.enter("lineEnding"), n.consume(s), n.exit("lineEnding"), w;
  }
  function w(s) {
    return s === null || C(s) ? P(s) : (n.enter("htmlFlowData"), S(s));
  }
  function U(s) {
    return s === 45 ? (n.consume(s), o) : S(s);
  }
  function W(s) {
    return s === 47 ? (n.consume(s), l = "", G) : S(s);
  }
  function G(s) {
    if (s === 62) {
      const K = l.toLowerCase();
      return Jn.includes(K) ? (n.consume(s), J) : S(s);
    }
    return nn(s) && l.length < 8 ? (n.consume(s), l += String.fromCharCode(s), G) : S(s);
  }
  function en(s) {
    return s === 93 ? (n.consume(s), o) : S(s);
  }
  function o(s) {
    return s === 62 ? (n.consume(s), J) : s === 45 && u === 2 ? (n.consume(s), o) : S(s);
  }
  function J(s) {
    return s === null || C(s) ? (n.exit("htmlFlowData"), rn(s)) : (n.consume(s), J);
  }
  function rn(s) {
    return n.exit("htmlFlow"), r(s);
  }
}
function Oe(n, r, t) {
  const e = this;
  return u;
  function u(l) {
    return C(l) ? (n.enter("lineEnding"), n.consume(l), n.exit("lineEnding"), i) : t(l);
  }
  function i(l) {
    return e.parser.lazy[e.now().line] ? t(l) : r(l);
  }
}
function De(n, r, t) {
  return e;
  function e(u) {
    return n.enter("lineEnding"), n.consume(u), n.exit("lineEnding"), n.attempt(Sn, r, t);
  }
}
const Pe = {
  name: "htmlText",
  tokenize: _e
};
function _e(n, r, t) {
  const e = this;
  let u, i, l;
  return a;
  function a(o) {
    return n.enter("htmlText"), n.enter("htmlTextData"), n.consume(o), m;
  }
  function m(o) {
    return o === 33 ? (n.consume(o), c) : o === 47 ? (n.consume(o), _) : o === 63 ? (n.consume(o), F) : nn(o) ? (n.consume(o), H) : t(o);
  }
  function c(o) {
    return o === 45 ? (n.consume(o), p) : o === 91 ? (n.consume(o), i = 0, A) : nn(o) ? (n.consume(o), j) : t(o);
  }
  function p(o) {
    return o === 45 ? (n.consume(o), h) : t(o);
  }
  function f(o) {
    return o === null ? t(o) : o === 45 ? (n.consume(o), x) : C(o) ? (l = f, W(o)) : (n.consume(o), f);
  }
  function x(o) {
    return o === 45 ? (n.consume(o), h) : f(o);
  }
  function h(o) {
    return o === 62 ? U(o) : o === 45 ? x(o) : f(o);
  }
  function A(o) {
    const J = "CDATA[";
    return o === J.charCodeAt(i++) ? (n.consume(o), i === J.length ? I : A) : t(o);
  }
  function I(o) {
    return o === null ? t(o) : o === 93 ? (n.consume(o), M) : C(o) ? (l = I, W(o)) : (n.consume(o), I);
  }
  function M(o) {
    return o === 93 ? (n.consume(o), b) : I(o);
  }
  function b(o) {
    return o === 62 ? U(o) : o === 93 ? (n.consume(o), b) : I(o);
  }
  function j(o) {
    return o === null || o === 62 ? U(o) : C(o) ? (l = j, W(o)) : (n.consume(o), j);
  }
  function F(o) {
    return o === null ? t(o) : o === 63 ? (n.consume(o), D) : C(o) ? (l = F, W(o)) : (n.consume(o), F);
  }
  function D(o) {
    return o === 62 ? U(o) : F(o);
  }
  function _(o) {
    return nn(o) ? (n.consume(o), k) : t(o);
  }
  function k(o) {
    return o === 45 || v(o) ? (n.consume(o), k) : T(o);
  }
  function T(o) {
    return C(o) ? (l = T, W(o)) : z(o) ? (n.consume(o), T) : U(o);
  }
  function H(o) {
    return o === 45 || v(o) ? (n.consume(o), H) : o === 47 || o === 62 || Z(o) ? N(o) : t(o);
  }
  function N(o) {
    return o === 47 ? (n.consume(o), U) : o === 58 || o === 95 || nn(o) ? (n.consume(o), V) : C(o) ? (l = N, W(o)) : z(o) ? (n.consume(o), N) : U(o);
  }
  function V(o) {
    return o === 45 || o === 46 || o === 58 || o === 95 || v(o) ? (n.consume(o), V) : y(o);
  }
  function y(o) {
    return o === 61 ? (n.consume(o), S) : C(o) ? (l = y, W(o)) : z(o) ? (n.consume(o), y) : N(o);
  }
  function S(o) {
    return o === null || o === 60 || o === 61 || o === 62 || o === 96 ? t(o) : o === 34 || o === 39 ? (n.consume(o), u = o, P) : C(o) ? (l = S, W(o)) : z(o) ? (n.consume(o), S) : (n.consume(o), R);
  }
  function P(o) {
    return o === u ? (n.consume(o), u = void 0, w) : o === null ? t(o) : C(o) ? (l = P, W(o)) : (n.consume(o), P);
  }
  function R(o) {
    return o === null || o === 34 || o === 39 || o === 60 || o === 61 || o === 96 ? t(o) : o === 47 || o === 62 || Z(o) ? N(o) : (n.consume(o), R);
  }
  function w(o) {
    return o === 47 || o === 62 || Z(o) ? N(o) : t(o);
  }
  function U(o) {
    return o === 62 ? (n.consume(o), n.exit("htmlTextData"), n.exit("htmlText"), r) : t(o);
  }
  function W(o) {
    return n.exit("htmlTextData"), n.enter("lineEnding"), n.consume(o), n.exit("lineEnding"), G;
  }
  function G(o) {
    return z(o) ? O(
      n,
      en,
      "linePrefix",
      e.parser.constructs.disable.null.includes("codeIndented") ? void 0 : 4
    )(o) : en(o);
  }
  function en(o) {
    return n.enter("htmlTextData"), l(o);
  }
}
const Dn = {
  name: "labelEnd",
  tokenize: Ne,
  resolveTo: He,
  resolveAll: qe
}, Me = {
  tokenize: Ve
}, je = {
  tokenize: We
}, Re = {
  tokenize: Qe
};
function qe(n) {
  let r = -1;
  for (; ++r < n.length; ) {
    const t = n[r][1];
    (t.type === "labelImage" || t.type === "labelLink" || t.type === "labelEnd") && (n.splice(r + 1, t.type === "labelImage" ? 4 : 2), t.type = "data", r++);
  }
  return n;
}
function He(n, r) {
  let t = n.length, e = 0, u, i, l, a;
  for (; t--; )
    if (u = n[t][1], i) {
      if (u.type === "link" || u.type === "labelLink" && u._inactive)
        break;
      n[t][0] === "enter" && u.type === "labelLink" && (u._inactive = !0);
    } else if (l) {
      if (n[t][0] === "enter" && (u.type === "labelImage" || u.type === "labelLink") && !u._balanced && (i = t, u.type !== "labelLink")) {
        e = 2;
        break;
      }
    } else
      u.type === "labelEnd" && (l = t);
  const m = {
    type: n[i][1].type === "labelLink" ? "link" : "image",
    start: Object.assign({}, n[i][1].start),
    end: Object.assign({}, n[n.length - 1][1].end)
  }, c = {
    type: "label",
    start: Object.assign({}, n[i][1].start),
    end: Object.assign({}, n[l][1].end)
  }, p = {
    type: "labelText",
    start: Object.assign({}, n[i + e + 2][1].end),
    end: Object.assign({}, n[l - 2][1].start)
  };
  return a = [
    ["enter", m, r],
    ["enter", c, r]
  ], a = Y(a, n.slice(i + 1, i + e + 3)), a = Y(a, [["enter", p, r]]), a = Y(
    a,
    Ln(
      r.parser.constructs.insideSpan.null,
      n.slice(i + e + 4, l - 3),
      r
    )
  ), a = Y(a, [
    ["exit", p, r],
    n[l - 2],
    n[l - 1],
    ["exit", c, r]
  ]), a = Y(a, n.slice(l + 1)), a = Y(a, [["exit", m, r]]), tn(n, i, n.length, a), n;
}
function Ne(n, r, t) {
  const e = this;
  let u = e.events.length, i, l;
  for (; u--; )
    if ((e.events[u][1].type === "labelImage" || e.events[u][1].type === "labelLink") && !e.events[u][1]._balanced) {
      i = e.events[u][1];
      break;
    }
  return a;
  function a(x) {
    return i ? i._inactive ? f(x) : (l = e.parser.defined.includes(
      xn(
        e.sliceSerialize({
          start: i.end,
          end: e.now()
        })
      )
    ), n.enter("labelEnd"), n.enter("labelMarker"), n.consume(x), n.exit("labelMarker"), n.exit("labelEnd"), m) : t(x);
  }
  function m(x) {
    return x === 40 ? n.attempt(
      Me,
      p,
      l ? p : f
    )(x) : x === 91 ? n.attempt(
      je,
      p,
      l ? c : f
    )(x) : l ? p(x) : f(x);
  }
  function c(x) {
    return n.attempt(
      Re,
      p,
      f
    )(x);
  }
  function p(x) {
    return r(x);
  }
  function f(x) {
    return i._balanced = !0, t(x);
  }
}
function Ve(n, r, t) {
  return e;
  function e(f) {
    return n.enter("resource"), n.enter("resourceMarker"), n.consume(f), n.exit("resourceMarker"), u;
  }
  function u(f) {
    return Z(f) ? dn(n, i)(f) : i(f);
  }
  function i(f) {
    return f === 41 ? p(f) : at(
      n,
      l,
      a,
      "resourceDestination",
      "resourceDestinationLiteral",
      "resourceDestinationLiteralMarker",
      "resourceDestinationRaw",
      "resourceDestinationString",
      32
    )(f);
  }
  function l(f) {
    return Z(f) ? dn(n, m)(f) : p(f);
  }
  function a(f) {
    return t(f);
  }
  function m(f) {
    return f === 34 || f === 39 || f === 40 ? st(
      n,
      c,
      t,
      "resourceTitle",
      "resourceTitleMarker",
      "resourceTitleString"
    )(f) : p(f);
  }
  function c(f) {
    return Z(f) ? dn(n, p)(f) : p(f);
  }
  function p(f) {
    return f === 41 ? (n.enter("resourceMarker"), n.consume(f), n.exit("resourceMarker"), n.exit("resource"), r) : t(f);
  }
}
function We(n, r, t) {
  const e = this;
  return u;
  function u(a) {
    return ot.call(
      e,
      n,
      i,
      l,
      "reference",
      "referenceMarker",
      "referenceString"
    )(a);
  }
  function i(a) {
    return e.parser.defined.includes(
      xn(
        e.sliceSerialize(e.events[e.events.length - 1][1]).slice(1, -1)
      )
    ) ? r(a) : t(a);
  }
  function l(a) {
    return t(a);
  }
}
function Qe(n, r, t) {
  return e;
  function e(i) {
    return n.enter("reference"), n.enter("referenceMarker"), n.consume(i), n.exit("referenceMarker"), u;
  }
  function u(i) {
    return i === 93 ? (n.enter("referenceMarker"), n.consume(i), n.exit("referenceMarker"), n.exit("reference"), r) : t(i);
  }
}
const Ue = {
  name: "labelStartImage",
  tokenize: $e,
  resolveAll: Dn.resolveAll
};
function $e(n, r, t) {
  const e = this;
  return u;
  function u(a) {
    return n.enter("labelImage"), n.enter("labelImageMarker"), n.consume(a), n.exit("labelImageMarker"), i;
  }
  function i(a) {
    return a === 91 ? (n.enter("labelMarker"), n.consume(a), n.exit("labelMarker"), n.exit("labelImage"), l) : t(a);
  }
  function l(a) {
    return a === 94 && "_hiddenFootnoteSupport" in e.parser.constructs ? t(a) : r(a);
  }
}
const Ze = {
  name: "labelStartLink",
  tokenize: Ye,
  resolveAll: Dn.resolveAll
};
function Ye(n, r, t) {
  const e = this;
  return u;
  function u(l) {
    return n.enter("labelLink"), n.enter("labelMarker"), n.consume(l), n.exit("labelMarker"), n.exit("labelLink"), i;
  }
  function i(l) {
    return l === 94 && "_hiddenFootnoteSupport" in e.parser.constructs ? t(l) : r(l);
  }
}
const wn = {
  name: "lineEnding",
  tokenize: Ge
};
function Ge(n, r) {
  return t;
  function t(e) {
    return n.enter("lineEnding"), n.consume(e), n.exit("lineEnding"), O(n, r, "linePrefix");
  }
}
const bn = {
  name: "thematicBreak",
  tokenize: Je
};
function Je(n, r, t) {
  let e = 0, u;
  return i;
  function i(c) {
    return n.enter("thematicBreak"), l(c);
  }
  function l(c) {
    return u = c, a(c);
  }
  function a(c) {
    return c === u ? (n.enter("thematicBreakSequence"), m(c)) : e >= 3 && (c === null || C(c)) ? (n.exit("thematicBreak"), r(c)) : t(c);
  }
  function m(c) {
    return c === u ? (n.consume(c), e++, m) : (n.exit("thematicBreakSequence"), z(c) ? O(n, a, "whitespace")(c) : a(c));
  }
}
const $ = {
  name: "list",
  tokenize: ve,
  continuation: {
    tokenize: nr
  },
  exit: er
}, Ke = {
  tokenize: rr,
  partial: !0
}, Xe = {
  tokenize: tr,
  partial: !0
};
function ve(n, r, t) {
  const e = this, u = e.events[e.events.length - 1];
  let i = u && u[1].type === "linePrefix" ? u[2].sliceSerialize(u[1], !0).length : 0, l = 0;
  return a;
  function a(h) {
    const A = e.containerState.type || (h === 42 || h === 43 || h === 45 ? "listUnordered" : "listOrdered");
    if (A === "listUnordered" ? !e.containerState.marker || h === e.containerState.marker : zn(h)) {
      if (e.containerState.type || (e.containerState.type = A, n.enter(A, {
        _container: !0
      })), A === "listUnordered")
        return n.enter("listItemPrefix"), h === 42 || h === 45 ? n.check(bn, t, c)(h) : c(h);
      if (!e.interrupt || h === 49)
        return n.enter("listItemPrefix"), n.enter("listItemValue"), m(h);
    }
    return t(h);
  }
  function m(h) {
    return zn(h) && ++l < 10 ? (n.consume(h), m) : (!e.interrupt || l < 2) && (e.containerState.marker ? h === e.containerState.marker : h === 41 || h === 46) ? (n.exit("listItemValue"), c(h)) : t(h);
  }
  function c(h) {
    return n.enter("listItemMarker"), n.consume(h), n.exit("listItemMarker"), e.containerState.marker = e.containerState.marker || h, n.check(
      Sn,
      // Can’t be empty when interrupting.
      e.interrupt ? t : p,
      n.attempt(
        Ke,
        x,
        f
      )
    );
  }
  function p(h) {
    return e.containerState.initialBlankLine = !0, i++, x(h);
  }
  function f(h) {
    return z(h) ? (n.enter("listItemPrefixWhitespace"), n.consume(h), n.exit("listItemPrefixWhitespace"), x) : t(h);
  }
  function x(h) {
    return e.containerState.size = i + e.sliceSerialize(n.exit("listItemPrefix"), !0).length, r(h);
  }
}
function nr(n, r, t) {
  const e = this;
  return e.containerState._closeFlow = void 0, n.check(Sn, u, i);
  function u(a) {
    return e.containerState.furtherBlankLines = e.containerState.furtherBlankLines || e.containerState.initialBlankLine, O(
      n,
      r,
      "listItemIndent",
      e.containerState.size + 1
    )(a);
  }
  function i(a) {
    return e.containerState.furtherBlankLines || !z(a) ? (e.containerState.furtherBlankLines = void 0, e.containerState.initialBlankLine = void 0, l(a)) : (e.containerState.furtherBlankLines = void 0, e.containerState.initialBlankLine = void 0, n.attempt(Xe, r, l)(a));
  }
  function l(a) {
    return e.containerState._closeFlow = !0, e.interrupt = void 0, O(
      n,
      n.attempt($, r, t),
      "linePrefix",
      e.parser.constructs.disable.null.includes("codeIndented") ? void 0 : 4
    )(a);
  }
}
function tr(n, r, t) {
  const e = this;
  return O(
    n,
    u,
    "listItemIndent",
    e.containerState.size + 1
  );
  function u(i) {
    const l = e.events[e.events.length - 1];
    return l && l[1].type === "listItemIndent" && l[2].sliceSerialize(l[1], !0).length === e.containerState.size ? r(i) : t(i);
  }
}
function er(n) {
  n.exit(this.containerState.type);
}
function rr(n, r, t) {
  const e = this;
  return O(
    n,
    u,
    "listItemPrefixWhitespace",
    e.parser.constructs.disable.null.includes("codeIndented") ? void 0 : 4 + 1
  );
  function u(i) {
    const l = e.events[e.events.length - 1];
    return !z(i) && l && l[1].type === "listItemPrefixWhitespace" ? r(i) : t(i);
  }
}
const Kn = {
  name: "setextUnderline",
  tokenize: ur,
  resolveTo: ir
};
function ir(n, r) {
  let t = n.length, e, u, i;
  for (; t--; )
    if (n[t][0] === "enter") {
      if (n[t][1].type === "content") {
        e = t;
        break;
      }
      n[t][1].type === "paragraph" && (u = t);
    } else
      n[t][1].type === "content" && n.splice(t, 1), !i && n[t][1].type === "definition" && (i = t);
  const l = {
    type: "setextHeading",
    start: Object.assign({}, n[u][1].start),
    end: Object.assign({}, n[n.length - 1][1].end)
  };
  return n[u][1].type = "setextHeadingText", i ? (n.splice(u, 0, ["enter", l, r]), n.splice(i + 1, 0, ["exit", n[e][1], r]), n[e][1].end = Object.assign({}, n[i][1].end)) : n[e][1] = l, n.push(["exit", l, r]), n;
}
function ur(n, r, t) {
  const e = this;
  let u;
  return i;
  function i(c) {
    let p = e.events.length, f;
    for (; p--; )
      if (e.events[p][1].type !== "lineEnding" && e.events[p][1].type !== "linePrefix" && e.events[p][1].type !== "content") {
        f = e.events[p][1].type === "paragraph";
        break;
      }
    return !e.parser.lazy[e.now().line] && (e.interrupt || f) ? (n.enter("setextHeadingLine"), u = c, l(c)) : t(c);
  }
  function l(c) {
    return n.enter("setextHeadingLineSequence"), a(c);
  }
  function a(c) {
    return c === u ? (n.consume(c), a) : (n.exit("setextHeadingLineSequence"), z(c) ? O(n, m, "lineSuffix")(c) : m(c));
  }
  function m(c) {
    return c === null || C(c) ? (n.exit("setextHeadingLine"), r(c)) : t(c);
  }
}
const lr = {
  tokenize: ar
};
function ar(n) {
  const r = this, t = n.attempt(
    // Try to parse a blank line.
    Sn,
    e,
    // Try to parse initial flow (essentially, only code).
    n.attempt(
      this.parser.constructs.flowInitial,
      u,
      O(
        n,
        n.attempt(
          this.parser.constructs.flow,
          u,
          n.attempt(pe, u)
        ),
        "linePrefix"
      )
    )
  );
  return t;
  function e(i) {
    if (i === null) {
      n.consume(i);
      return;
    }
    return n.enter("lineEndingBlank"), n.consume(i), n.exit("lineEndingBlank"), r.currentConstruct = void 0, t;
  }
  function u(i) {
    if (i === null) {
      n.consume(i);
      return;
    }
    return n.enter("lineEnding"), n.consume(i), n.exit("lineEnding"), r.currentConstruct = void 0, t;
  }
}
const or = {
  resolveAll: ht()
}, sr = ct("string"), cr = ct("text");
function ct(n) {
  return {
    tokenize: r,
    resolveAll: ht(
      n === "text" ? hr : void 0
    )
  };
  function r(t) {
    const e = this, u = this.parser.constructs[n], i = t.attempt(u, l, a);
    return l;
    function l(p) {
      return c(p) ? i(p) : a(p);
    }
    function a(p) {
      if (p === null) {
        t.consume(p);
        return;
      }
      return t.enter("data"), t.consume(p), m;
    }
    function m(p) {
      return c(p) ? (t.exit("data"), i(p)) : (t.consume(p), m);
    }
    function c(p) {
      if (p === null)
        return !0;
      const f = u[p];
      let x = -1;
      if (f)
        for (; ++x < f.length; ) {
          const h = f[x];
          if (!h.previous || h.previous.call(e, e.previous))
            return !0;
        }
      return !1;
    }
  }
}
function ht(n) {
  return r;
  function r(t, e) {
    let u = -1, i;
    for (; ++u <= t.length; )
      i === void 0 ? t[u] && t[u][1].type === "data" && (i = u, u++) : (!t[u] || t[u][1].type !== "data") && (u !== i + 2 && (t[i][1].end = t[u - 1][1].end, t.splice(i + 2, u - i - 2), u = i + 2), i = void 0);
    return n ? n(t, e) : t;
  }
}
function hr(n, r) {
  let t = 0;
  for (; ++t <= n.length; )
    if ((t === n.length || n[t][1].type === "lineEnding") && n[t - 1][1].type === "data") {
      const e = n[t - 1][1], u = r.sliceStream(e);
      let i = u.length, l = -1, a = 0, m;
      for (; i--; ) {
        const c = u[i];
        if (typeof c == "string") {
          for (l = c.length; c.charCodeAt(l - 1) === 32; )
            a++, l--;
          if (l)
            break;
          l = -1;
        } else if (c === -2)
          m = !0, a++;
        else if (c !== -1) {
          i++;
          break;
        }
      }
      if (a) {
        const c = {
          type: t === n.length || m || a < 2 ? "lineSuffix" : "hardBreakTrailing",
          start: {
            line: e.end.line,
            column: e.end.column - a,
            offset: e.end.offset - a,
            _index: e.start._index + i,
            _bufferIndex: i ? l : e.start._bufferIndex + l
          },
          end: Object.assign({}, e.end)
        };
        e.end = Object.assign({}, c.start), e.start.offset === e.end.offset ? Object.assign(e, c) : (n.splice(
          t,
          0,
          ["enter", c, r],
          ["exit", c, r]
        ), t += 2);
      }
      t++;
    }
  return n;
}
function pr(n, r, t) {
  let e = Object.assign(
    t ? Object.assign({}, t) : {
      line: 1,
      column: 1,
      offset: 0
    },
    {
      _index: 0,
      _bufferIndex: -1
    }
  );
  const u = {}, i = [];
  let l = [], a = [];
  const m = {
    consume: j,
    enter: F,
    exit: D,
    attempt: T(_),
    check: T(k),
    interrupt: T(k, {
      interrupt: !0
    })
  }, c = {
    previous: null,
    code: null,
    containerState: {},
    events: [],
    parser: n,
    sliceStream: h,
    sliceSerialize: x,
    now: A,
    defineSkip: I,
    write: f
  };
  let p = r.tokenize.call(c, m);
  return r.resolveAll && i.push(r), c;
  function f(y) {
    return l = Y(l, y), M(), l[l.length - 1] !== null ? [] : (H(r, 0), c.events = Ln(i, c.events, c), c.events);
  }
  function x(y, S) {
    return mr(h(y), S);
  }
  function h(y) {
    return fr(l, y);
  }
  function A() {
    const { line: y, column: S, offset: P, _index: R, _bufferIndex: w } = e;
    return {
      line: y,
      column: S,
      offset: P,
      _index: R,
      _bufferIndex: w
    };
  }
  function I(y) {
    u[y.line] = y.column, V();
  }
  function M() {
    let y;
    for (; e._index < l.length; ) {
      const S = l[e._index];
      if (typeof S == "string")
        for (y = e._index, e._bufferIndex < 0 && (e._bufferIndex = 0); e._index === y && e._bufferIndex < S.length; )
          b(S.charCodeAt(e._bufferIndex));
      else
        b(S);
    }
  }
  function b(y) {
    p = p(y);
  }
  function j(y) {
    C(y) ? (e.line++, e.column = 1, e.offset += y === -3 ? 2 : 1, V()) : y !== -1 && (e.column++, e.offset++), e._bufferIndex < 0 ? e._index++ : (e._bufferIndex++, e._bufferIndex === l[e._index].length && (e._bufferIndex = -1, e._index++)), c.previous = y;
  }
  function F(y, S) {
    const P = S || {};
    return P.type = y, P.start = A(), c.events.push(["enter", P, c]), a.push(P), P;
  }
  function D(y) {
    const S = a.pop();
    return S.end = A(), c.events.push(["exit", S, c]), S;
  }
  function _(y, S) {
    H(y, S.from);
  }
  function k(y, S) {
    S.restore();
  }
  function T(y, S) {
    return P;
    function P(R, w, U) {
      let W, G, en, o;
      return Array.isArray(R) ? rn(R) : "tokenize" in R ? (
        // @ts-expect-error Looks like a construct.
        rn([R])
      ) : J(R);
      function J(Q) {
        return pn;
        function pn(an) {
          const fn = an !== null && Q[an], mn = an !== null && Q.null, Fn = [
            // To do: add more extension tests.
            /* c8 ignore next 2 */
            ...Array.isArray(fn) ? fn : fn ? [fn] : [],
            ...Array.isArray(mn) ? mn : mn ? [mn] : []
          ];
          return rn(Fn)(an);
        }
      }
      function rn(Q) {
        return W = Q, G = 0, Q.length === 0 ? U : s(Q[G]);
      }
      function s(Q) {
        return pn;
        function pn(an) {
          return o = N(), en = Q, Q.partial || (c.currentConstruct = Q), Q.name && c.parser.constructs.disable.null.includes(Q.name) ? hn() : Q.tokenize.call(
            // If we do have fields, create an object w/ `context` as its
            // prototype.
            // This allows a “live binding”, which is needed for `interrupt`.
            S ? Object.assign(Object.create(c), S) : c,
            m,
            K,
            hn
          )(an);
        }
      }
      function K(Q) {
        return y(en, o), w;
      }
      function hn(Q) {
        return o.restore(), ++G < W.length ? s(W[G]) : U;
      }
    }
  }
  function H(y, S) {
    y.resolveAll && !i.includes(y) && i.push(y), y.resolve && tn(
      c.events,
      S,
      c.events.length - S,
      y.resolve(c.events.slice(S), c)
    ), y.resolveTo && (c.events = y.resolveTo(c.events, c));
  }
  function N() {
    const y = A(), S = c.previous, P = c.currentConstruct, R = c.events.length, w = Array.from(a);
    return {
      restore: U,
      from: R
    };
    function U() {
      e = y, c.previous = S, c.currentConstruct = P, c.events.length = R, a = w, V();
    }
  }
  function V() {
    e.line in u && e.column < 2 && (e.column = u[e.line], e.offset += u[e.line] - 1);
  }
}
function fr(n, r) {
  const t = r.start._index, e = r.start._bufferIndex, u = r.end._index, i = r.end._bufferIndex;
  let l;
  if (t === u)
    l = [n[t].slice(e, i)];
  else {
    if (l = n.slice(t, u), e > -1) {
      const a = l[0];
      typeof a == "string" ? l[0] = a.slice(e) : l.shift();
    }
    i > 0 && l.push(n[u].slice(0, i));
  }
  return l;
}
function mr(n, r) {
  let t = -1;
  const e = [];
  let u;
  for (; ++t < n.length; ) {
    const i = n[t];
    let l;
    if (typeof i == "string")
      l = i;
    else
      switch (i) {
        case -5: {
          l = "\r";
          break;
        }
        case -4: {
          l = `
`;
          break;
        }
        case -3: {
          l = `\r
`;
          break;
        }
        case -2: {
          l = r ? " " : "	";
          break;
        }
        case -1: {
          if (!r && u)
            continue;
          l = " ";
          break;
        }
        default:
          l = String.fromCharCode(i);
      }
    u = i === -2, e.push(l);
  }
  return e.join("");
}
const xr = {
  42: $,
  43: $,
  45: $,
  48: $,
  49: $,
  50: $,
  51: $,
  52: $,
  53: $,
  54: $,
  55: $,
  56: $,
  57: $,
  62: rt
}, gr = {
  91: ke
}, kr = {
  [-2]: Cn,
  [-1]: Cn,
  32: Cn
}, dr = {
  35: Ee,
  42: bn,
  45: [Kn, bn],
  60: ze,
  61: Kn,
  95: bn,
  96: Gn,
  126: Gn
}, br = {
  38: ut,
  92: it
}, yr = {
  [-5]: wn,
  [-4]: wn,
  [-3]: wn,
  33: Ue,
  38: ut,
  42: In,
  60: [Yt, Pe],
  91: Ze,
  92: [Se, it],
  93: Dn,
  95: In,
  96: ae
}, Sr = {
  null: [In, or]
}, Fr = {
  null: [42, 95]
}, Er = {
  null: []
}, Cr = /* @__PURE__ */ Object.freeze(/* @__PURE__ */ Object.defineProperty({
  __proto__: null,
  attentionMarkers: Fr,
  contentInitial: gr,
  disable: Er,
  document: xr,
  flow: dr,
  flowInitial: kr,
  insideSpan: Sr,
  string: br,
  text: yr
}, Symbol.toStringTag, { value: "Module" }));
function wr(n) {
  const t = (
    /** @type {FullNormalizedExtension} */
    Ot([Cr, ...(n || {}).extensions || []])
  ), e = {
    defined: [],
    lazy: {},
    constructs: t,
    content: u(Nt),
    document: u(Wt),
    flow: u(lr),
    string: u(sr),
    text: u(cr)
  };
  return e;
  function u(i) {
    return l;
    function l(a) {
      return pr(e, i, a);
    }
  }
}
const Xn = /[\0\t\n\r]/g;
function Ar() {
  let n = 1, r = "", t = !0, e;
  return u;
  function u(i, l, a) {
    const m = [];
    let c, p, f, x, h;
    for (i = r + i.toString(l), f = 0, r = "", t && (i.charCodeAt(0) === 65279 && f++, t = void 0); f < i.length; ) {
      if (Xn.lastIndex = f, c = Xn.exec(i), x = c && c.index !== void 0 ? c.index : i.length, h = i.charCodeAt(x), !c) {
        r = i.slice(f);
        break;
      }
      if (h === 10 && f === x && e)
        m.push(-3), e = void 0;
      else
        switch (e && (m.push(-5), e = void 0), f < x && (m.push(i.slice(f, x)), n += x - f), h) {
          case 0: {
            m.push(65533), n++;
            break;
          }
          case 9: {
            for (p = Math.ceil(n / 4) * 4, m.push(-2); n++ < p; )
              m.push(-1);
            break;
          }
          case 10: {
            m.push(-4), n = 1;
            break;
          }
          default:
            e = !0, n = 1;
        }
      f = x + 1;
    }
    return a && (e && m.push(-5), r && m.push(r), m.push(null)), m;
  }
}
function zr(n) {
  for (; !lt(n); )
    ;
  return n;
}
function pt(n, r) {
  const t = Number.parseInt(n, r);
  return (
    // C0 except for HT, LF, FF, CR, space.
    t < 9 || t === 11 || t > 13 && t < 32 || // Control character (DEL) of C0, and C1 controls.
    t > 126 && t < 160 || // Lone high surrogates and low surrogates.
    t > 55295 && t < 57344 || // Noncharacters.
    t > 64975 && t < 65008 || (t & 65535) === 65535 || (t & 65535) === 65534 || // Out of range
    t > 1114111 ? "�" : String.fromCharCode(t)
  );
}
const Ir = /\\([!-/:-@[-`{-~])|&(#(?:\d{1,7}|x[\da-f]{1,6})|[\da-z]{1,31});/gi;
function Tr(n) {
  return n.replace(Ir, Br);
}
function Br(n, r, t) {
  if (r)
    return r;
  if (t.charCodeAt(0) === 35) {
    const u = t.charCodeAt(1), i = u === 120 || u === 88;
    return pt(t.slice(i ? 2 : 1), i ? 16 : 10);
  }
  return On(t) || n;
}
function yn(n) {
  return !n || typeof n != "object" ? "" : "position" in n || "type" in n ? vn(n.position) : "start" in n || "end" in n ? vn(n) : "line" in n || "column" in n ? Tn(n) : "";
}
function Tn(n) {
  return nt(n && n.line) + ":" + nt(n && n.column);
}
function vn(n) {
  return Tn(n && n.start) + "-" + Tn(n && n.end);
}
function nt(n) {
  return n && typeof n == "number" ? n : 1;
}
const ft = {}.hasOwnProperty, mt = (
  /**
   * @type {(
   *   ((value: Value, encoding: Encoding, options?: Options | null | undefined) => Root) &
   *   ((value: Value, options?: Options | null | undefined) => Root)
   * )}
   */
  /**
   * @param {Value} value
   * @param {Encoding | Options | null | undefined} [encoding]
   * @param {Options | null | undefined} [options]
   * @returns {Root}
   */
  function(n, r, t) {
    return typeof r != "string" && (t = r, r = void 0), Lr(t)(
      zr(
        // @ts-expect-error: micromark types need to accept `null`.
        wr(t).document().write(Ar()(n, r, !0))
      )
    );
  }
);
function Lr(n) {
  const r = {
    transforms: [],
    canContainEols: ["emphasis", "fragment", "heading", "paragraph", "strong"],
    enter: {
      autolink: a(Hn),
      autolinkProtocol: y,
      autolinkEmail: y,
      atxHeading: a(jn),
      blockQuote: a(Fn),
      characterEscape: y,
      characterReference: y,
      codeFenced: a(Mn),
      codeFencedFenceInfo: m,
      codeFencedFenceMeta: m,
      codeIndented: a(Mn, m),
      codeText: a(kt, m),
      codeTextData: y,
      data: y,
      codeFlowValue: y,
      definition: a(dt),
      definitionDestinationString: m,
      definitionLabelString: m,
      definitionTitleString: m,
      emphasis: a(bt),
      hardBreakEscape: a(Rn),
      hardBreakTrailing: a(Rn),
      htmlFlow: a(qn, m),
      htmlFlowData: y,
      htmlText: a(qn, m),
      htmlTextData: y,
      image: a(yt),
      label: m,
      link: a(Hn),
      listItem: a(St),
      listItemValue: A,
      listOrdered: a(Nn, h),
      listUnordered: a(Nn),
      paragraph: a(Ft),
      reference: hn,
      referenceString: m,
      resourceDestinationString: m,
      resourceTitleString: m,
      setextHeading: a(jn),
      strong: a(Et),
      thematicBreak: a(wt)
    },
    exit: {
      atxHeading: p(),
      atxHeadingSequence: T,
      autolink: p(),
      autolinkEmail: mn,
      autolinkProtocol: fn,
      blockQuote: p(),
      characterEscapeValue: S,
      characterReferenceMarkerHexadecimal: pn,
      characterReferenceMarkerNumeric: pn,
      characterReferenceValue: an,
      codeFenced: p(j),
      codeFencedFence: b,
      codeFencedFenceInfo: I,
      codeFencedFenceMeta: M,
      codeFlowValue: S,
      codeIndented: p(F),
      codeText: p(W),
      codeTextData: S,
      data: S,
      definition: p(),
      definitionDestinationString: k,
      definitionLabelString: D,
      definitionTitleString: _,
      emphasis: p(),
      hardBreakEscape: p(R),
      hardBreakTrailing: p(R),
      htmlFlow: p(w),
      htmlFlowData: S,
      htmlText: p(U),
      htmlTextData: S,
      image: p(en),
      label: J,
      labelText: o,
      lineEnding: P,
      link: p(G),
      listItem: p(),
      listOrdered: p(),
      listUnordered: p(),
      paragraph: p(),
      referenceString: Q,
      resourceDestinationString: rn,
      resourceTitleString: s,
      resource: K,
      setextHeading: p(V),
      setextHeadingLineSequence: N,
      setextHeadingText: H,
      strong: p(),
      thematicBreak: p()
    }
  };
  xt(r, (n || {}).mdastExtensions || []);
  const t = {};
  return e;
  function e(g) {
    let d = {
      type: "root",
      children: []
    };
    const E = {
      stack: [d],
      tokenStack: [],
      config: r,
      enter: c,
      exit: f,
      buffer: m,
      resume: x,
      setData: i,
      getData: l
    }, B = [];
    let L = -1;
    for (; ++L < g.length; )
      if (g[L][1].type === "listOrdered" || g[L][1].type === "listUnordered")
        if (g[L][0] === "enter")
          B.push(L);
        else {
          const X = B.pop();
          L = u(g, X, L);
        }
    for (L = -1; ++L < g.length; ) {
      const X = r[g[L][0]];
      ft.call(X, g[L][1].type) && X[g[L][1].type].call(
        Object.assign(
          {
            sliceSerialize: g[L][2].sliceSerialize
          },
          E
        ),
        g[L][1]
      );
    }
    if (E.tokenStack.length > 0) {
      const X = E.tokenStack[E.tokenStack.length - 1];
      (X[1] || tt).call(E, void 0, X[0]);
    }
    for (d.position = {
      start: sn(
        g.length > 0 ? g[0][1].start : {
          line: 1,
          column: 1,
          offset: 0
        }
      ),
      end: sn(
        g.length > 0 ? g[g.length - 2][1].end : {
          line: 1,
          column: 1,
          offset: 0
        }
      )
    }, L = -1; ++L < r.transforms.length; )
      d = r.transforms[L](d) || d;
    return d;
  }
  function u(g, d, E) {
    let B = d - 1, L = -1, X = !1, on, un, gn, kn;
    for (; ++B <= E; ) {
      const q = g[B];
      if (q[1].type === "listUnordered" || q[1].type === "listOrdered" || q[1].type === "blockQuote" ? (q[0] === "enter" ? L++ : L--, kn = void 0) : q[1].type === "lineEndingBlank" ? q[0] === "enter" && (on && !kn && !L && !gn && (gn = B), kn = void 0) : q[1].type === "linePrefix" || q[1].type === "listItemValue" || q[1].type === "listItemMarker" || q[1].type === "listItemPrefix" || q[1].type === "listItemPrefixWhitespace" || (kn = void 0), !L && q[0] === "enter" && q[1].type === "listItemPrefix" || L === -1 && q[0] === "exit" && (q[1].type === "listUnordered" || q[1].type === "listOrdered")) {
        if (on) {
          let En = B;
          for (un = void 0; En--; ) {
            const ln = g[En];
            if (ln[1].type === "lineEnding" || ln[1].type === "lineEndingBlank") {
              if (ln[0] === "exit")
                continue;
              un && (g[un][1].type = "lineEndingBlank", X = !0), ln[1].type = "lineEnding", un = En;
            } else if (!(ln[1].type === "linePrefix" || ln[1].type === "blockQuotePrefix" || ln[1].type === "blockQuotePrefixWhitespace" || ln[1].type === "blockQuoteMarker" || ln[1].type === "listItemIndent"))
              break;
          }
          gn && (!un || gn < un) && (on._spread = !0), on.end = Object.assign(
            {},
            un ? g[un][1].start : q[1].end
          ), g.splice(un || B, 0, ["exit", on, q[2]]), B++, E++;
        }
        q[1].type === "listItemPrefix" && (on = {
          type: "listItem",
          // @ts-expect-error Patched
          _spread: !1,
          start: Object.assign({}, q[1].start)
        }, g.splice(B, 0, ["enter", on, q[2]]), B++, E++, gn = void 0, kn = !0);
      }
    }
    return g[d][1]._spread = X, E;
  }
  function i(g, d) {
    t[g] = d;
  }
  function l(g) {
    return t[g];
  }
  function a(g, d) {
    return E;
    function E(B) {
      c.call(this, g(B), B), d && d.call(this, B);
    }
  }
  function m() {
    this.stack.push({
      type: "fragment",
      children: []
    });
  }
  function c(g, d, E) {
    return this.stack[this.stack.length - 1].children.push(g), this.stack.push(g), this.tokenStack.push([d, E]), g.position = {
      start: sn(d.start)
    }, g;
  }
  function p(g) {
    return d;
    function d(E) {
      g && g.call(this, E), f.call(this, E);
    }
  }
  function f(g, d) {
    const E = this.stack.pop(), B = this.tokenStack.pop();
    if (B)
      B[0].type !== g.type && (d ? d.call(this, g, B[0]) : (B[1] || tt).call(this, g, B[0]));
    else
      throw new Error(
        "Cannot close `" + g.type + "` (" + yn({
          start: g.start,
          end: g.end
        }) + "): it’s not open"
      );
    return E.position.end = sn(g.end), E;
  }
  function x() {
    return Bt(this.stack.pop());
  }
  function h() {
    i("expectingFirstListItemValue", !0);
  }
  function A(g) {
    if (l("expectingFirstListItemValue")) {
      const d = this.stack[this.stack.length - 2];
      d.start = Number.parseInt(this.sliceSerialize(g), 10), i("expectingFirstListItemValue");
    }
  }
  function I() {
    const g = this.resume(), d = this.stack[this.stack.length - 1];
    d.lang = g;
  }
  function M() {
    const g = this.resume(), d = this.stack[this.stack.length - 1];
    d.meta = g;
  }
  function b() {
    l("flowCodeInside") || (this.buffer(), i("flowCodeInside", !0));
  }
  function j() {
    const g = this.resume(), d = this.stack[this.stack.length - 1];
    d.value = g.replace(/^(\r?\n|\r)|(\r?\n|\r)$/g, ""), i("flowCodeInside");
  }
  function F() {
    const g = this.resume(), d = this.stack[this.stack.length - 1];
    d.value = g.replace(/(\r?\n|\r)$/g, "");
  }
  function D(g) {
    const d = this.resume(), E = this.stack[this.stack.length - 1];
    E.label = d, E.identifier = xn(
      this.sliceSerialize(g)
    ).toLowerCase();
  }
  function _() {
    const g = this.resume(), d = this.stack[this.stack.length - 1];
    d.title = g;
  }
  function k() {
    const g = this.resume(), d = this.stack[this.stack.length - 1];
    d.url = g;
  }
  function T(g) {
    const d = this.stack[this.stack.length - 1];
    if (!d.depth) {
      const E = this.sliceSerialize(g).length;
      d.depth = E;
    }
  }
  function H() {
    i("setextHeadingSlurpLineEnding", !0);
  }
  function N(g) {
    const d = this.stack[this.stack.length - 1];
    d.depth = this.sliceSerialize(g).charCodeAt(0) === 61 ? 1 : 2;
  }
  function V() {
    i("setextHeadingSlurpLineEnding");
  }
  function y(g) {
    const d = this.stack[this.stack.length - 1];
    let E = d.children[d.children.length - 1];
    (!E || E.type !== "text") && (E = Ct(), E.position = {
      start: sn(g.start)
    }, d.children.push(E)), this.stack.push(E);
  }
  function S(g) {
    const d = this.stack.pop();
    d.value += this.sliceSerialize(g), d.position.end = sn(g.end);
  }
  function P(g) {
    const d = this.stack[this.stack.length - 1];
    if (l("atHardBreak")) {
      const E = d.children[d.children.length - 1];
      E.position.end = sn(g.end), i("atHardBreak");
      return;
    }
    !l("setextHeadingSlurpLineEnding") && r.canContainEols.includes(d.type) && (y.call(this, g), S.call(this, g));
  }
  function R() {
    i("atHardBreak", !0);
  }
  function w() {
    const g = this.resume(), d = this.stack[this.stack.length - 1];
    d.value = g;
  }
  function U() {
    const g = this.resume(), d = this.stack[this.stack.length - 1];
    d.value = g;
  }
  function W() {
    const g = this.resume(), d = this.stack[this.stack.length - 1];
    d.value = g;
  }
  function G() {
    const g = this.stack[this.stack.length - 1];
    if (l("inReference")) {
      const d = l("referenceType") || "shortcut";
      g.type += "Reference", g.referenceType = d, delete g.url, delete g.title;
    } else
      delete g.identifier, delete g.label;
    i("referenceType");
  }
  function en() {
    const g = this.stack[this.stack.length - 1];
    if (l("inReference")) {
      const d = l("referenceType") || "shortcut";
      g.type += "Reference", g.referenceType = d, delete g.url, delete g.title;
    } else
      delete g.identifier, delete g.label;
    i("referenceType");
  }
  function o(g) {
    const d = this.sliceSerialize(g), E = this.stack[this.stack.length - 2];
    E.label = Tr(d), E.identifier = xn(d).toLowerCase();
  }
  function J() {
    const g = this.stack[this.stack.length - 1], d = this.resume(), E = this.stack[this.stack.length - 1];
    if (i("inReference", !0), E.type === "link") {
      const B = g.children;
      E.children = B;
    } else
      E.alt = d;
  }
  function rn() {
    const g = this.resume(), d = this.stack[this.stack.length - 1];
    d.url = g;
  }
  function s() {
    const g = this.resume(), d = this.stack[this.stack.length - 1];
    d.title = g;
  }
  function K() {
    i("inReference");
  }
  function hn() {
    i("referenceType", "collapsed");
  }
  function Q(g) {
    const d = this.resume(), E = this.stack[this.stack.length - 1];
    E.label = d, E.identifier = xn(
      this.sliceSerialize(g)
    ).toLowerCase(), i("referenceType", "full");
  }
  function pn(g) {
    i("characterReferenceType", g.type);
  }
  function an(g) {
    const d = this.sliceSerialize(g), E = l("characterReferenceType");
    let B;
    E ? (B = pt(
      d,
      E === "characterReferenceMarkerNumeric" ? 10 : 16
    ), i("characterReferenceType")) : B = On(d);
    const L = this.stack.pop();
    L.value += B, L.position.end = sn(g.end);
  }
  function fn(g) {
    S.call(this, g);
    const d = this.stack[this.stack.length - 1];
    d.url = this.sliceSerialize(g);
  }
  function mn(g) {
    S.call(this, g);
    const d = this.stack[this.stack.length - 1];
    d.url = "mailto:" + this.sliceSerialize(g);
  }
  function Fn() {
    return {
      type: "blockquote",
      children: []
    };
  }
  function Mn() {
    return {
      type: "code",
      lang: null,
      meta: null,
      value: ""
    };
  }
  function kt() {
    return {
      type: "inlineCode",
      value: ""
    };
  }
  function dt() {
    return {
      type: "definition",
      identifier: "",
      label: null,
      title: null,
      url: ""
    };
  }
  function bt() {
    return {
      type: "emphasis",
      children: []
    };
  }
  function jn() {
    return {
      type: "heading",
      depth: void 0,
      children: []
    };
  }
  function Rn() {
    return {
      type: "break"
    };
  }
  function qn() {
    return {
      type: "html",
      value: ""
    };
  }
  function yt() {
    return {
      type: "image",
      title: null,
      url: "",
      alt: null
    };
  }
  function Hn() {
    return {
      type: "link",
      title: null,
      url: "",
      children: []
    };
  }
  function Nn(g) {
    return {
      type: "list",
      ordered: g.type === "listOrdered",
      start: null,
      // @ts-expect-error Patched.
      spread: g._spread,
      children: []
    };
  }
  function St(g) {
    return {
      type: "listItem",
      // @ts-expect-error Patched.
      spread: g._spread,
      checked: null,
      children: []
    };
  }
  function Ft() {
    return {
      type: "paragraph",
      children: []
    };
  }
  function Et() {
    return {
      type: "strong",
      children: []
    };
  }
  function Ct() {
    return {
      type: "text",
      value: ""
    };
  }
  function wt() {
    return {
      type: "thematicBreak"
    };
  }
}
function sn(n) {
  return {
    line: n.line,
    column: n.column,
    offset: n.offset
  };
}
function xt(n, r) {
  let t = -1;
  for (; ++t < r.length; ) {
    const e = r[t];
    Array.isArray(e) ? xt(n, e) : Or(n, e);
  }
}
function Or(n, r) {
  let t;
  for (t in r)
    if (ft.call(r, t)) {
      if (t === "canContainEols") {
        const e = r[t];
        e && n[t].push(...e);
      } else if (t === "transforms") {
        const e = r[t];
        e && n[t].push(...e);
      } else if (t === "enter" || t === "exit") {
        const e = r[t];
        e && Object.assign(n[t], e);
      }
    }
}
function tt(n, r) {
  throw n ? new Error(
    "Cannot close `" + n.type + "` (" + yn({
      start: n.start,
      end: n.end
    }) + "): a different token (`" + r.type + "`, " + yn({
      start: r.start,
      end: r.end
    }) + ") is open"
  ) : new Error(
    "Cannot close document, a token (`" + r.type + "`, " + yn({
      start: r.start,
      end: r.end
    }) + ") is still open"
  );
}
function Dr(n) {
  const r = n.replace(/\n{2,}/g, `
`);
  return At(r);
}
function Pr(n) {
  const r = Dr(n), { children: t } = mt(r), e = [[]];
  let u = 0;
  function i(l, a = "normal") {
    l.type === "text" ? l.value.split(`
`).forEach((c, p) => {
      p !== 0 && (u++, e.push([])), c.split(" ").forEach((f) => {
        f && e[u].push({ content: f, type: a });
      });
    }) : (l.type === "strong" || l.type === "emphasis") && l.children.forEach((m) => {
      i(m, l.type);
    });
  }
  return t.forEach((l) => {
    l.type === "paragraph" && l.children.forEach((a) => {
      i(a);
    });
  }), e;
}
function _r(n) {
  const { children: r } = mt(n);
  function t(e) {
    return e.type === "text" ? e.value.replace(/\n/g, "<br/>") : e.type === "strong" ? `<strong>${e.children.map(t).join("")}</strong>` : e.type === "emphasis" ? `<em>${e.children.map(t).join("")}</em>` : e.type === "paragraph" ? `<p>${e.children.map(t).join("")}</p>` : `Unsupported markdown: ${e.type}`;
  }
  return r.map(t).join("");
}
function Mr(n) {
  return Intl.Segmenter ? [...new Intl.Segmenter().segment(n)].map((r) => r.segment) : [...n];
}
function jr(n, r) {
  const t = Mr(r.content);
  return gt(n, [], t, r.type);
}
function gt(n, r, t, e) {
  if (t.length === 0)
    return [
      { content: r.join(""), type: e },
      { content: "", type: e }
    ];
  const [u, ...i] = t, l = [...r, u];
  return n([{ content: l.join(""), type: e }]) ? gt(n, l, i, e) : (r.length === 0 && u && (r.push(u), t.shift()), [
    { content: r.join(""), type: e },
    { content: t.join(""), type: e }
  ]);
}
function Rr(n, r) {
  if (n.some(({ content: t }) => t.includes(`
`)))
    throw new Error("splitLineToFitWidth does not support newlines in the line");
  return Bn(n, r);
}
function Bn(n, r, t = [], e = []) {
  if (n.length === 0)
    return e.length > 0 && t.push(e), t.length > 0 ? t : [];
  let u = "";
  n[0].content === " " && (u = " ", n.shift());
  const i = n.shift() ?? { content: " ", type: "normal" }, l = [...e];
  if (u !== "" && l.push({ content: u, type: "normal" }), l.push(i), r(l))
    return Bn(n, r, t, l);
  if (e.length > 0)
    t.push(e), n.unshift(i);
  else if (i.content) {
    const [a, m] = jr(r, i);
    t.push([a]), m.content && n.unshift(m);
  }
  return Bn(n, r, t);
}
function qr(n, r) {
  r && n.attr("style", r);
}
function Hr(n, r, t, e, u = !1) {
  const i = n.append("foreignObject"), l = i.append("xhtml:div"), a = r.label, m = r.isNode ? "nodeLabel" : "edgeLabel";
  l.html(
    `
    <span class="${m} ${e}" ` + (r.labelStyle ? 'style="' + r.labelStyle + '"' : "") + ">" + a + "</span>"
  ), qr(l, r.labelStyle), l.style("display", "table-cell"), l.style("white-space", "nowrap"), l.style("max-width", t + "px"), l.attr("xmlns", "http://www.w3.org/1999/xhtml"), u && l.attr("class", "labelBkg");
  let c = l.node().getBoundingClientRect();
  return c.width === t && (l.style("display", "table"), l.style("white-space", "break-spaces"), l.style("width", t + "px"), c = l.node().getBoundingClientRect()), i.style("width", c.width), i.style("height", c.height), i.node();
}
function Pn(n, r, t) {
  return n.append("tspan").attr("class", "text-outer-tspan").attr("x", 0).attr("y", r * t - 0.1 + "em").attr("dy", t + "em");
}
function Nr(n, r, t) {
  const e = n.append("text"), u = Pn(e, 1, r);
  _n(u, t);
  const i = u.node().getComputedTextLength();
  return e.remove(), i;
}
function Qr(n, r, t) {
  var l;
  const e = n.append("text"), u = Pn(e, 1, r);
  _n(u, [{ content: t, type: "normal" }]);
  const i = (l = u.node()) == null ? void 0 : l.getBoundingClientRect();
  return i && e.remove(), i;
}
function Vr(n, r, t, e = !1) {
  const i = r.append("g"), l = i.insert("rect").attr("class", "background"), a = i.append("text").attr("y", "-10.1");
  let m = 0;
  for (const c of t) {
    const p = (x) => Nr(i, 1.1, x) <= n, f = p(c) ? [c] : Rr(c, p);
    for (const x of f) {
      const h = Pn(a, m, 1.1);
      _n(h, x), m++;
    }
  }
  if (e) {
    const c = a.node().getBBox(), p = 2;
    return l.attr("x", -p).attr("y", -p).attr("width", c.width + 2 * p).attr("height", c.height + 2 * p), i.node();
  } else
    return a.node();
}
function _n(n, r) {
  n.text(""), r.forEach((t, e) => {
    const u = n.append("tspan").attr("font-style", t.type === "emphasis" ? "italic" : "normal").attr("class", "text-inner-tspan").attr("font-weight", t.type === "strong" ? "bold" : "normal");
    e === 0 ? u.text(t.content) : u.text(" " + t.content);
  });
}
const Ur = (n, r = "", {
  style: t = "",
  isTitle: e = !1,
  classes: u = "",
  useHtmlLabels: i = !0,
  isNode: l = !0,
  width: a = 200,
  addSvgBackground: m = !1
} = {}) => {
  if (zt.info("createText", r, t, e, u, i, l, m), i) {
    const c = _r(r), p = {
      isNode: l,
      label: It(c).replace(
        /fa[blrs]?:fa-[\w-]+/g,
        (x) => `<i class='${x.replace(":", " ")}'></i>`
      ),
      labelStyle: t.replace("fill:", "color:")
    };
    return Hr(n, p, a, u, m);
  } else {
    const c = Pr(r);
    return Vr(a, n, c, m);
  }
};
export {
  Ur as a,
  Qr as c
};
