import { l as wt, s as zt, g as Ft, B as Nt, C as St, a as Xt, b as Yt, Y as Ht, Z as ot, W as Ct, V as Ut, D as $t, d as qt, T as jt, k as Gt } from "./mermaid-a09fe7cd.js";
import { c as Qt } from "./createText-e916aecc.js";
import { i as Kt } from "./init-f9637058.js";
import { o as Zt } from "./ordinal-5695958c.js";
import { l as ft } from "./linear-2bc336bd.js";
import { l as pt } from "./line-0f31738a.js";
import "./array-2ff2c7a6.js";
import "./path-428ebac9.js";
function Jt(e, t, i) {
  e = +e, t = +t, i = (n = arguments.length) < 2 ? (t = e, e = 0, 1) : n < 3 ? 1 : +i;
  for (var s = -1, n = Math.max(0, Math.ceil((t - e) / i)) | 0, o = new Array(n); ++s < n; )
    o[s] = e + s * i;
  return o;
}
function st() {
  var e = Zt().unknown(void 0), t = e.domain, i = e.range, s = 0, n = 1, o, c, f = !1, d = 0, R = 0, _ = 0.5;
  delete e.unknown;
  function A() {
    var m = t().length, T = n < s, S = T ? n : s, P = T ? s : n;
    o = (P - S) / Math.max(1, m - d + R * 2), f && (o = Math.floor(o)), S += (P - S - o * (m - d)) * _, c = o * (1 - d), f && (S = Math.round(S), c = Math.round(c));
    var p = Jt(m).map(function(C) {
      return S + o * C;
    });
    return i(T ? p.reverse() : p);
  }
  return e.domain = function(m) {
    return arguments.length ? (t(m), A()) : t();
  }, e.range = function(m) {
    return arguments.length ? ([s, n] = m, s = +s, n = +n, A()) : [s, n];
  }, e.rangeRound = function(m) {
    return [s, n] = m, s = +s, n = +n, f = !0, A();
  }, e.bandwidth = function() {
    return c;
  }, e.step = function() {
    return o;
  }, e.round = function(m) {
    return arguments.length ? (f = !!m, A()) : f;
  }, e.padding = function(m) {
    return arguments.length ? (d = Math.min(1, R = +m), A()) : d;
  }, e.paddingInner = function(m) {
    return arguments.length ? (d = Math.min(1, m), A()) : d;
  }, e.paddingOuter = function(m) {
    return arguments.length ? (R = +m, A()) : R;
  }, e.align = function(m) {
    return arguments.length ? (_ = Math.max(0, Math.min(1, m)), A()) : _;
  }, e.copy = function() {
    return st(t(), [s, n]).round(f).paddingInner(d).paddingOuter(R).align(_);
  }, Kt.apply(A(), arguments);
}
var nt = function() {
  var e = function(V, r, l, u) {
    for (l = l || {}, u = V.length; u--; l[V[u]] = r)
      ;
    return l;
  }, t = [1, 10, 12, 14, 16, 18, 19, 21, 23], i = [2, 6], s = [1, 3], n = [1, 5], o = [1, 6], c = [1, 7], f = [1, 5, 10, 12, 14, 16, 18, 19, 21, 23, 34, 35, 36], d = [1, 25], R = [1, 26], _ = [1, 28], A = [1, 29], m = [1, 30], T = [1, 31], S = [1, 32], P = [1, 33], p = [1, 34], C = [1, 35], h = [1, 36], L = [1, 37], z = [1, 43], lt = [1, 42], ct = [1, 47], U = [1, 50], w = [1, 10, 12, 14, 16, 18, 19, 21, 23, 34, 35, 36], Q = [1, 10, 12, 14, 16, 18, 19, 21, 23, 24, 26, 27, 28, 34, 35, 36], E = [1, 10, 12, 14, 16, 18, 19, 21, 23, 24, 26, 27, 28, 34, 35, 36, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], ut = [1, 64], K = {
    trace: function() {
    },
    yy: {},
    symbols_: { error: 2, start: 3, eol: 4, XYCHART: 5, chartConfig: 6, document: 7, CHART_ORIENTATION: 8, statement: 9, title: 10, text: 11, X_AXIS: 12, parseXAxis: 13, Y_AXIS: 14, parseYAxis: 15, LINE: 16, plotData: 17, BAR: 18, acc_title: 19, acc_title_value: 20, acc_descr: 21, acc_descr_value: 22, acc_descr_multiline_value: 23, SQUARE_BRACES_START: 24, commaSeparatedNumbers: 25, SQUARE_BRACES_END: 26, NUMBER_WITH_DECIMAL: 27, COMMA: 28, xAxisData: 29, bandData: 30, ARROW_DELIMITER: 31, commaSeparatedTexts: 32, yAxisData: 33, NEWLINE: 34, SEMI: 35, EOF: 36, alphaNum: 37, STR: 38, MD_STR: 39, alphaNumToken: 40, AMP: 41, NUM: 42, ALPHA: 43, PLUS: 44, EQUALS: 45, MULT: 46, DOT: 47, BRKT: 48, MINUS: 49, UNDERSCORE: 50, $accept: 0, $end: 1 },
    terminals_: { 2: "error", 5: "XYCHART", 8: "CHART_ORIENTATION", 10: "title", 12: "X_AXIS", 14: "Y_AXIS", 16: "LINE", 18: "BAR", 19: "acc_title", 20: "acc_title_value", 21: "acc_descr", 22: "acc_descr_value", 23: "acc_descr_multiline_value", 24: "SQUARE_BRACES_START", 26: "SQUARE_BRACES_END", 27: "NUMBER_WITH_DECIMAL", 28: "COMMA", 31: "ARROW_DELIMITER", 34: "NEWLINE", 35: "SEMI", 36: "EOF", 38: "STR", 39: "MD_STR", 41: "AMP", 42: "NUM", 43: "ALPHA", 44: "PLUS", 45: "EQUALS", 46: "MULT", 47: "DOT", 48: "BRKT", 49: "MINUS", 50: "UNDERSCORE" },
    productions_: [0, [3, 2], [3, 3], [3, 2], [3, 1], [6, 1], [7, 0], [7, 2], [9, 2], [9, 2], [9, 2], [9, 2], [9, 2], [9, 3], [9, 2], [9, 3], [9, 2], [9, 2], [9, 1], [17, 3], [25, 3], [25, 1], [13, 1], [13, 2], [13, 1], [29, 1], [29, 3], [30, 3], [32, 3], [32, 1], [15, 1], [15, 2], [15, 1], [33, 3], [4, 1], [4, 1], [4, 1], [11, 1], [11, 1], [11, 1], [37, 1], [37, 2], [40, 1], [40, 1], [40, 1], [40, 1], [40, 1], [40, 1], [40, 1], [40, 1], [40, 1], [40, 1]],
    performAction: function(r, l, u, g, b, a, F) {
      var x = a.length - 1;
      switch (b) {
        case 5:
          g.setOrientation(a[x]);
          break;
        case 9:
          g.setDiagramTitle(a[x].text.trim());
          break;
        case 12:
          g.setLineData({ text: "", type: "text" }, a[x]);
          break;
        case 13:
          g.setLineData(a[x - 1], a[x]);
          break;
        case 14:
          g.setBarData({ text: "", type: "text" }, a[x]);
          break;
        case 15:
          g.setBarData(a[x - 1], a[x]);
          break;
        case 16:
          this.$ = a[x].trim(), g.setAccTitle(this.$);
          break;
        case 17:
        case 18:
          this.$ = a[x].trim(), g.setAccDescription(this.$);
          break;
        case 19:
          this.$ = a[x - 1];
          break;
        case 20:
          this.$ = [Number(a[x - 2]), ...a[x]];
          break;
        case 21:
          this.$ = [Number(a[x])];
          break;
        case 22:
          g.setXAxisTitle(a[x]);
          break;
        case 23:
          g.setXAxisTitle(a[x - 1]);
          break;
        case 24:
          g.setXAxisTitle({ type: "text", text: "" });
          break;
        case 25:
          g.setXAxisBand(a[x]);
          break;
        case 26:
          g.setXAxisRangeData(Number(a[x - 2]), Number(a[x]));
          break;
        case 27:
          this.$ = a[x - 1];
          break;
        case 28:
          this.$ = [a[x - 2], ...a[x]];
          break;
        case 29:
          this.$ = [a[x]];
          break;
        case 30:
          g.setYAxisTitle(a[x]);
          break;
        case 31:
          g.setYAxisTitle(a[x - 1]);
          break;
        case 32:
          g.setYAxisTitle({ type: "text", text: "" });
          break;
        case 33:
          g.setYAxisRangeData(Number(a[x - 2]), Number(a[x]));
          break;
        case 37:
          this.$ = { text: a[x], type: "text" };
          break;
        case 38:
          this.$ = { text: a[x], type: "text" };
          break;
        case 39:
          this.$ = { text: a[x], type: "markdown" };
          break;
        case 40:
          this.$ = a[x];
          break;
        case 41:
          this.$ = a[x - 1] + "" + a[x];
          break;
      }
    },
    table: [e(t, i, { 3: 1, 4: 2, 7: 4, 5: s, 34: n, 35: o, 36: c }), { 1: [3] }, e(t, i, { 4: 2, 7: 4, 3: 8, 5: s, 34: n, 35: o, 36: c }), e(t, i, { 4: 2, 7: 4, 6: 9, 3: 10, 5: s, 8: [1, 11], 34: n, 35: o, 36: c }), { 1: [2, 4], 9: 12, 10: [1, 13], 12: [1, 14], 14: [1, 15], 16: [1, 16], 18: [1, 17], 19: [1, 18], 21: [1, 19], 23: [1, 20] }, e(f, [2, 34]), e(f, [2, 35]), e(f, [2, 36]), { 1: [2, 1] }, e(t, i, { 4: 2, 7: 4, 3: 21, 5: s, 34: n, 35: o, 36: c }), { 1: [2, 3] }, e(f, [2, 5]), e(t, [2, 7], { 4: 22, 34: n, 35: o, 36: c }), { 11: 23, 37: 24, 38: d, 39: R, 40: 27, 41: _, 42: A, 43: m, 44: T, 45: S, 46: P, 47: p, 48: C, 49: h, 50: L }, { 11: 39, 13: 38, 24: z, 27: lt, 29: 40, 30: 41, 37: 24, 38: d, 39: R, 40: 27, 41: _, 42: A, 43: m, 44: T, 45: S, 46: P, 47: p, 48: C, 49: h, 50: L }, { 11: 45, 15: 44, 27: ct, 33: 46, 37: 24, 38: d, 39: R, 40: 27, 41: _, 42: A, 43: m, 44: T, 45: S, 46: P, 47: p, 48: C, 49: h, 50: L }, { 11: 49, 17: 48, 24: U, 37: 24, 38: d, 39: R, 40: 27, 41: _, 42: A, 43: m, 44: T, 45: S, 46: P, 47: p, 48: C, 49: h, 50: L }, { 11: 52, 17: 51, 24: U, 37: 24, 38: d, 39: R, 40: 27, 41: _, 42: A, 43: m, 44: T, 45: S, 46: P, 47: p, 48: C, 49: h, 50: L }, { 20: [1, 53] }, { 22: [1, 54] }, e(w, [2, 18]), { 1: [2, 2] }, e(w, [2, 8]), e(w, [2, 9]), e(Q, [2, 37], { 40: 55, 41: _, 42: A, 43: m, 44: T, 45: S, 46: P, 47: p, 48: C, 49: h, 50: L }), e(Q, [2, 38]), e(Q, [2, 39]), e(E, [2, 40]), e(E, [2, 42]), e(E, [2, 43]), e(E, [2, 44]), e(E, [2, 45]), e(E, [2, 46]), e(E, [2, 47]), e(E, [2, 48]), e(E, [2, 49]), e(E, [2, 50]), e(E, [2, 51]), e(w, [2, 10]), e(w, [2, 22], { 30: 41, 29: 56, 24: z, 27: lt }), e(w, [2, 24]), e(w, [2, 25]), { 31: [1, 57] }, { 11: 59, 32: 58, 37: 24, 38: d, 39: R, 40: 27, 41: _, 42: A, 43: m, 44: T, 45: S, 46: P, 47: p, 48: C, 49: h, 50: L }, e(w, [2, 11]), e(w, [2, 30], { 33: 60, 27: ct }), e(w, [2, 32]), { 31: [1, 61] }, e(w, [2, 12]), { 17: 62, 24: U }, { 25: 63, 27: ut }, e(w, [2, 14]), { 17: 65, 24: U }, e(w, [2, 16]), e(w, [2, 17]), e(E, [2, 41]), e(w, [2, 23]), { 27: [1, 66] }, { 26: [1, 67] }, { 26: [2, 29], 28: [1, 68] }, e(w, [2, 31]), { 27: [1, 69] }, e(w, [2, 13]), { 26: [1, 70] }, { 26: [2, 21], 28: [1, 71] }, e(w, [2, 15]), e(w, [2, 26]), e(w, [2, 27]), { 11: 59, 32: 72, 37: 24, 38: d, 39: R, 40: 27, 41: _, 42: A, 43: m, 44: T, 45: S, 46: P, 47: p, 48: C, 49: h, 50: L }, e(w, [2, 33]), e(w, [2, 19]), { 25: 73, 27: ut }, { 26: [2, 28] }, { 26: [2, 20] }],
    defaultActions: { 8: [2, 1], 10: [2, 3], 21: [2, 2], 72: [2, 28], 73: [2, 20] },
    parseError: function(r, l) {
      if (l.recoverable)
        this.trace(r);
      else {
        var u = new Error(r);
        throw u.hash = l, u;
      }
    },
    parse: function(r) {
      var l = this, u = [0], g = [], b = [null], a = [], F = this.table, x = "", $ = 0, gt = 0, Vt = 2, xt = 1, Bt = a.slice.call(arguments, 1), k = Object.create(this.lexer), B = { yy: {} };
      for (var J in this.yy)
        Object.prototype.hasOwnProperty.call(this.yy, J) && (B.yy[J] = this.yy[J]);
      k.setInput(r, B.yy), B.yy.lexer = k, B.yy.parser = this, typeof k.yylloc > "u" && (k.yylloc = {});
      var tt = k.yylloc;
      a.push(tt);
      var Wt = k.options && k.options.ranges;
      typeof B.yy.parseError == "function" ? this.parseError = B.yy.parseError : this.parseError = Object.getPrototypeOf(this).parseError;
      function Ot() {
        var I;
        return I = g.pop() || k.lex() || xt, typeof I != "number" && (I instanceof Array && (g = I, I = g.pop()), I = l.symbols_[I] || I), I;
      }
      for (var D, W, v, it, O = {}, q, M, dt, j; ; ) {
        if (W = u[u.length - 1], this.defaultActions[W] ? v = this.defaultActions[W] : ((D === null || typeof D > "u") && (D = Ot()), v = F[W] && F[W][D]), typeof v > "u" || !v.length || !v[0]) {
          var et = "";
          j = [];
          for (q in F[W])
            this.terminals_[q] && q > Vt && j.push("'" + this.terminals_[q] + "'");
          k.showPosition ? et = "Parse error on line " + ($ + 1) + `:
` + k.showPosition() + `
Expecting ` + j.join(", ") + ", got '" + (this.terminals_[D] || D) + "'" : et = "Parse error on line " + ($ + 1) + ": Unexpected " + (D == xt ? "end of input" : "'" + (this.terminals_[D] || D) + "'"), this.parseError(et, {
            text: k.match,
            token: this.terminals_[D] || D,
            line: k.yylineno,
            loc: tt,
            expected: j
          });
        }
        if (v[0] instanceof Array && v.length > 1)
          throw new Error("Parse Error: multiple actions possible at state: " + W + ", token: " + D);
        switch (v[0]) {
          case 1:
            u.push(D), b.push(k.yytext), a.push(k.yylloc), u.push(v[1]), D = null, gt = k.yyleng, x = k.yytext, $ = k.yylineno, tt = k.yylloc;
            break;
          case 2:
            if (M = this.productions_[v[1]][1], O.$ = b[b.length - M], O._$ = {
              first_line: a[a.length - (M || 1)].first_line,
              last_line: a[a.length - 1].last_line,
              first_column: a[a.length - (M || 1)].first_column,
              last_column: a[a.length - 1].last_column
            }, Wt && (O._$.range = [
              a[a.length - (M || 1)].range[0],
              a[a.length - 1].range[1]
            ]), it = this.performAction.apply(O, [
              x,
              gt,
              $,
              B.yy,
              v[1],
              b,
              a
            ].concat(Bt)), typeof it < "u")
              return it;
            M && (u = u.slice(0, -1 * M * 2), b = b.slice(0, -1 * M), a = a.slice(0, -1 * M)), u.push(this.productions_[v[1]][0]), b.push(O.$), a.push(O._$), dt = F[u[u.length - 2]][u[u.length - 1]], u.push(dt);
            break;
          case 3:
            return !0;
        }
      }
      return !0;
    }
  }, It = function() {
    var V = {
      EOF: 1,
      parseError: function(l, u) {
        if (this.yy.parser)
          this.yy.parser.parseError(l, u);
        else
          throw new Error(l);
      },
      // resets the lexer, sets new input
      setInput: function(r, l) {
        return this.yy = l || this.yy || {}, this._input = r, this._more = this._backtrack = this.done = !1, this.yylineno = this.yyleng = 0, this.yytext = this.matched = this.match = "", this.conditionStack = ["INITIAL"], this.yylloc = {
          first_line: 1,
          first_column: 0,
          last_line: 1,
          last_column: 0
        }, this.options.ranges && (this.yylloc.range = [0, 0]), this.offset = 0, this;
      },
      // consumes and returns one char from the input
      input: function() {
        var r = this._input[0];
        this.yytext += r, this.yyleng++, this.offset++, this.match += r, this.matched += r;
        var l = r.match(/(?:\r\n?|\n).*/g);
        return l ? (this.yylineno++, this.yylloc.last_line++) : this.yylloc.last_column++, this.options.ranges && this.yylloc.range[1]++, this._input = this._input.slice(1), r;
      },
      // unshifts one char (or a string) into the input
      unput: function(r) {
        var l = r.length, u = r.split(/(?:\r\n?|\n)/g);
        this._input = r + this._input, this.yytext = this.yytext.substr(0, this.yytext.length - l), this.offset -= l;
        var g = this.match.split(/(?:\r\n?|\n)/g);
        this.match = this.match.substr(0, this.match.length - 1), this.matched = this.matched.substr(0, this.matched.length - 1), u.length - 1 && (this.yylineno -= u.length - 1);
        var b = this.yylloc.range;
        return this.yylloc = {
          first_line: this.yylloc.first_line,
          last_line: this.yylineno + 1,
          first_column: this.yylloc.first_column,
          last_column: u ? (u.length === g.length ? this.yylloc.first_column : 0) + g[g.length - u.length].length - u[0].length : this.yylloc.first_column - l
        }, this.options.ranges && (this.yylloc.range = [b[0], b[0] + this.yyleng - l]), this.yyleng = this.yytext.length, this;
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
      less: function(r) {
        this.unput(this.match.slice(r));
      },
      // displays already matched input, i.e. for error messages
      pastInput: function() {
        var r = this.matched.substr(0, this.matched.length - this.match.length);
        return (r.length > 20 ? "..." : "") + r.substr(-20).replace(/\n/g, "");
      },
      // displays upcoming input, i.e. for error messages
      upcomingInput: function() {
        var r = this.match;
        return r.length < 20 && (r += this._input.substr(0, 20 - r.length)), (r.substr(0, 20) + (r.length > 20 ? "..." : "")).replace(/\n/g, "");
      },
      // displays the character position where the lexing error occurred, i.e. for error messages
      showPosition: function() {
        var r = this.pastInput(), l = new Array(r.length + 1).join("-");
        return r + this.upcomingInput() + `
` + l + "^";
      },
      // test the lexed token: return FALSE when not a match, otherwise return token
      test_match: function(r, l) {
        var u, g, b;
        if (this.options.backtrack_lexer && (b = {
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
        }, this.options.ranges && (b.yylloc.range = this.yylloc.range.slice(0))), g = r[0].match(/(?:\r\n?|\n).*/g), g && (this.yylineno += g.length), this.yylloc = {
          first_line: this.yylloc.last_line,
          last_line: this.yylineno + 1,
          first_column: this.yylloc.last_column,
          last_column: g ? g[g.length - 1].length - g[g.length - 1].match(/\r?\n?/)[0].length : this.yylloc.last_column + r[0].length
        }, this.yytext += r[0], this.match += r[0], this.matches = r, this.yyleng = this.yytext.length, this.options.ranges && (this.yylloc.range = [this.offset, this.offset += this.yyleng]), this._more = !1, this._backtrack = !1, this._input = this._input.slice(r[0].length), this.matched += r[0], u = this.performAction.call(this, this.yy, this, l, this.conditionStack[this.conditionStack.length - 1]), this.done && this._input && (this.done = !1), u)
          return u;
        if (this._backtrack) {
          for (var a in b)
            this[a] = b[a];
          return !1;
        }
        return !1;
      },
      // return next match in input
      next: function() {
        if (this.done)
          return this.EOF;
        this._input || (this.done = !0);
        var r, l, u, g;
        this._more || (this.yytext = "", this.match = "");
        for (var b = this._currentRules(), a = 0; a < b.length; a++)
          if (u = this._input.match(this.rules[b[a]]), u && (!l || u[0].length > l[0].length)) {
            if (l = u, g = a, this.options.backtrack_lexer) {
              if (r = this.test_match(u, b[a]), r !== !1)
                return r;
              if (this._backtrack) {
                l = !1;
                continue;
              } else
                return !1;
            } else if (!this.options.flex)
              break;
          }
        return l ? (r = this.test_match(l, b[g]), r !== !1 ? r : !1) : this._input === "" ? this.EOF : this.parseError("Lexical error on line " + (this.yylineno + 1) + `. Unrecognized text.
` + this.showPosition(), {
          text: "",
          token: null,
          line: this.yylineno
        });
      },
      // return next match that has a token
      lex: function() {
        var l = this.next();
        return l || this.lex();
      },
      // activates a new lexer condition state (pushes the new lexer condition state onto the condition stack)
      begin: function(l) {
        this.conditionStack.push(l);
      },
      // pop the previously active lexer condition state off the condition stack
      popState: function() {
        var l = this.conditionStack.length - 1;
        return l > 0 ? this.conditionStack.pop() : this.conditionStack[0];
      },
      // produce the lexer rule set which is active for the currently active lexer condition state
      _currentRules: function() {
        return this.conditionStack.length && this.conditionStack[this.conditionStack.length - 1] ? this.conditions[this.conditionStack[this.conditionStack.length - 1]].rules : this.conditions.INITIAL.rules;
      },
      // return the currently active lexer condition state; when an index argument is provided it produces the N-th previous condition state, if available
      topState: function(l) {
        return l = this.conditionStack.length - 1 - Math.abs(l || 0), l >= 0 ? this.conditionStack[l] : "INITIAL";
      },
      // alias for begin(condition)
      pushState: function(l) {
        this.begin(l);
      },
      // return the number of states currently on the stack
      stateStackSize: function() {
        return this.conditionStack.length;
      },
      options: { "case-insensitive": !0 },
      performAction: function(l, u, g, b) {
        switch (g) {
          case 0:
            break;
          case 1:
            break;
          case 2:
            return this.popState(), 34;
          case 3:
            return this.popState(), 34;
          case 4:
            return 34;
          case 5:
            break;
          case 6:
            return 10;
          case 7:
            return this.pushState("acc_title"), 19;
          case 8:
            return this.popState(), "acc_title_value";
          case 9:
            return this.pushState("acc_descr"), 21;
          case 10:
            return this.popState(), "acc_descr_value";
          case 11:
            this.pushState("acc_descr_multiline");
            break;
          case 12:
            this.popState();
            break;
          case 13:
            return "acc_descr_multiline_value";
          case 14:
            return 5;
          case 15:
            return 8;
          case 16:
            return this.pushState("axis_data"), "X_AXIS";
          case 17:
            return this.pushState("axis_data"), "Y_AXIS";
          case 18:
            return this.pushState("axis_band_data"), 24;
          case 19:
            return 31;
          case 20:
            return this.pushState("data"), 16;
          case 21:
            return this.pushState("data"), 18;
          case 22:
            return this.pushState("data_inner"), 24;
          case 23:
            return 27;
          case 24:
            return this.popState(), 26;
          case 25:
            this.popState();
            break;
          case 26:
            this.pushState("string");
            break;
          case 27:
            this.popState();
            break;
          case 28:
            return "STR";
          case 29:
            return 24;
          case 30:
            return 26;
          case 31:
            return 43;
          case 32:
            return "COLON";
          case 33:
            return 44;
          case 34:
            return 28;
          case 35:
            return 45;
          case 36:
            return 46;
          case 37:
            return 48;
          case 38:
            return 50;
          case 39:
            return 47;
          case 40:
            return 41;
          case 41:
            return 49;
          case 42:
            return 42;
          case 43:
            break;
          case 44:
            return 35;
          case 45:
            return 36;
        }
      },
      rules: [/^(?:%%(?!\{)[^\n]*)/i, /^(?:[^\}]%%[^\n]*)/i, /^(?:(\r?\n))/i, /^(?:(\r?\n))/i, /^(?:[\n\r]+)/i, /^(?:%%[^\n]*)/i, /^(?:title\b)/i, /^(?:accTitle\s*:\s*)/i, /^(?:(?!\n||)*[^\n]*)/i, /^(?:accDescr\s*:\s*)/i, /^(?:(?!\n||)*[^\n]*)/i, /^(?:accDescr\s*\{\s*)/i, /^(?:\{)/i, /^(?:[^\}]*)/i, /^(?:xychart-beta\b)/i, /^(?:(?:vertical|horizontal))/i, /^(?:x-axis\b)/i, /^(?:y-axis\b)/i, /^(?:\[)/i, /^(?:-->)/i, /^(?:line\b)/i, /^(?:bar\b)/i, /^(?:\[)/i, /^(?:[+-]?(?:\d+(?:\.\d+)?|\.\d+))/i, /^(?:\])/i, /^(?:(?:`\)                                    \{ this\.pushState\(md_string\); \}\n<md_string>\(\?:\(\?!`"\)\.\)\+                  \{ return MD_STR; \}\n<md_string>\(\?:`))/i, /^(?:["])/i, /^(?:["])/i, /^(?:[^"]*)/i, /^(?:\[)/i, /^(?:\])/i, /^(?:[A-Za-z]+)/i, /^(?::)/i, /^(?:\+)/i, /^(?:,)/i, /^(?:=)/i, /^(?:\*)/i, /^(?:#)/i, /^(?:[\_])/i, /^(?:\.)/i, /^(?:&)/i, /^(?:-)/i, /^(?:[0-9]+)/i, /^(?:\s+)/i, /^(?:;)/i, /^(?:$)/i],
      conditions: { data_inner: { rules: [0, 1, 4, 5, 6, 7, 9, 11, 14, 15, 16, 17, 20, 21, 23, 24, 25, 26, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45], inclusive: !0 }, data: { rules: [0, 1, 3, 4, 5, 6, 7, 9, 11, 14, 15, 16, 17, 20, 21, 22, 25, 26, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45], inclusive: !0 }, axis_band_data: { rules: [0, 1, 4, 5, 6, 7, 9, 11, 14, 15, 16, 17, 20, 21, 24, 25, 26, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45], inclusive: !0 }, axis_data: { rules: [0, 1, 2, 4, 5, 6, 7, 9, 11, 14, 15, 16, 17, 18, 19, 20, 21, 23, 25, 26, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45], inclusive: !0 }, acc_descr_multiline: { rules: [12, 13], inclusive: !1 }, acc_descr: { rules: [10], inclusive: !1 }, acc_title: { rules: [8], inclusive: !1 }, title: { rules: [], inclusive: !1 }, md_string: { rules: [], inclusive: !1 }, string: { rules: [27, 28], inclusive: !1 }, INITIAL: { rules: [0, 1, 4, 5, 6, 7, 9, 11, 14, 15, 16, 17, 20, 21, 25, 26, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45], inclusive: !0 } }
    };
    return V;
  }();
  K.lexer = It;
  function Z() {
    this.yy = {};
  }
  return Z.prototype = K, K.Parser = Z, new Z();
}();
nt.parser = nt;
const ti = nt;
function mt(e) {
  return e.type === "bar";
}
function _t(e) {
  return e.type === "band";
}
function N(e) {
  return e.type === "linear";
}
class kt {
  constructor(t) {
    this.parentGroup = t;
  }
  getMaxDimension(t, i) {
    if (!this.parentGroup)
      return {
        width: t.reduce((o, c) => Math.max(c.length, o), 0) * i,
        height: i
      };
    const s = {
      width: 0,
      height: 0
    }, n = this.parentGroup.append("g").attr("visibility", "hidden").attr("font-size", i);
    for (const o of t) {
      const c = Qt(n, 1, o), f = c ? c.width : o.length * i, d = c ? c.height : i;
      s.width = Math.max(s.width, f), s.height = Math.max(s.height, d);
    }
    return n.remove(), s;
  }
}
const yt = 0.7, bt = 0.2;
class Rt {
  constructor(t, i, s, n) {
    this.axisConfig = t, this.title = i, this.textDimensionCalculator = s, this.axisThemeConfig = n, this.boundingRect = { x: 0, y: 0, width: 0, height: 0 }, this.axisPosition = "left", this.showTitle = !1, this.showLabel = !1, this.showTick = !1, this.showAxisLine = !1, this.outerPadding = 0, this.titleTextHeight = 0, this.labelTextHeight = 0, this.range = [0, 10], this.boundingRect = { x: 0, y: 0, width: 0, height: 0 }, this.axisPosition = "left";
  }
  setRange(t) {
    this.range = t, this.axisPosition === "left" || this.axisPosition === "right" ? this.boundingRect.height = t[1] - t[0] : this.boundingRect.width = t[1] - t[0], this.recalculateScale();
  }
  getRange() {
    return [this.range[0] + this.outerPadding, this.range[1] - this.outerPadding];
  }
  setAxisPosition(t) {
    this.axisPosition = t, this.setRange(this.range);
  }
  getTickDistance() {
    const t = this.getRange();
    return Math.abs(t[0] - t[1]) / this.getTickValues().length;
  }
  getAxisOuterPadding() {
    return this.outerPadding;
  }
  getLabelDimension() {
    return this.textDimensionCalculator.getMaxDimension(
      this.getTickValues().map((t) => t.toString()),
      this.axisConfig.labelFontSize
    );
  }
  recalculateOuterPaddingToDrawBar() {
    yt * this.getTickDistance() > this.outerPadding * 2 && (this.outerPadding = Math.floor(yt * this.getTickDistance() / 2)), this.recalculateScale();
  }
  calculateSpaceIfDrawnHorizontally(t) {
    let i = t.height;
    if (this.axisConfig.showAxisLine && i > this.axisConfig.axisLineWidth && (i -= this.axisConfig.axisLineWidth, this.showAxisLine = !0), this.axisConfig.showLabel) {
      const s = this.getLabelDimension(), n = bt * t.width;
      this.outerPadding = Math.min(s.width / 2, n);
      const o = s.height + this.axisConfig.labelPadding * 2;
      this.labelTextHeight = s.height, o <= i && (i -= o, this.showLabel = !0);
    }
    if (this.axisConfig.showTick && i >= this.axisConfig.tickLength && (this.showTick = !0, i -= this.axisConfig.tickLength), this.axisConfig.showTitle && this.title) {
      const s = this.textDimensionCalculator.getMaxDimension(
        [this.title],
        this.axisConfig.titleFontSize
      ), n = s.height + this.axisConfig.titlePadding * 2;
      this.titleTextHeight = s.height, n <= i && (i -= n, this.showTitle = !0);
    }
    this.boundingRect.width = t.width, this.boundingRect.height = t.height - i;
  }
  calculateSpaceIfDrawnVertical(t) {
    let i = t.width;
    if (this.axisConfig.showAxisLine && i > this.axisConfig.axisLineWidth && (i -= this.axisConfig.axisLineWidth, this.showAxisLine = !0), this.axisConfig.showLabel) {
      const s = this.getLabelDimension(), n = bt * t.height;
      this.outerPadding = Math.min(s.height / 2, n);
      const o = s.width + this.axisConfig.labelPadding * 2;
      o <= i && (i -= o, this.showLabel = !0);
    }
    if (this.axisConfig.showTick && i >= this.axisConfig.tickLength && (this.showTick = !0, i -= this.axisConfig.tickLength), this.axisConfig.showTitle && this.title) {
      const s = this.textDimensionCalculator.getMaxDimension(
        [this.title],
        this.axisConfig.titleFontSize
      ), n = s.height + this.axisConfig.titlePadding * 2;
      this.titleTextHeight = s.height, n <= i && (i -= n, this.showTitle = !0);
    }
    this.boundingRect.width = t.width - i, this.boundingRect.height = t.height;
  }
  calculateSpace(t) {
    return this.axisPosition === "left" || this.axisPosition === "right" ? this.calculateSpaceIfDrawnVertical(t) : this.calculateSpaceIfDrawnHorizontally(t), this.recalculateScale(), {
      width: this.boundingRect.width,
      height: this.boundingRect.height
    };
  }
  setBoundingBoxXY(t) {
    this.boundingRect.x = t.x, this.boundingRect.y = t.y;
  }
  getDrawableElementsForLeftAxis() {
    const t = [];
    if (this.showAxisLine) {
      const i = this.boundingRect.x + this.boundingRect.width - this.axisConfig.axisLineWidth / 2;
      t.push({
        type: "path",
        groupTexts: ["left-axis", "axisl-line"],
        data: [
          {
            path: `M ${i},${this.boundingRect.y} L ${i},${this.boundingRect.y + this.boundingRect.height} `,
            strokeFill: this.axisThemeConfig.axisLineColor,
            strokeWidth: this.axisConfig.axisLineWidth
          }
        ]
      });
    }
    if (this.showLabel && t.push({
      type: "text",
      groupTexts: ["left-axis", "label"],
      data: this.getTickValues().map((i) => ({
        text: i.toString(),
        x: this.boundingRect.x + this.boundingRect.width - (this.showLabel ? this.axisConfig.labelPadding : 0) - (this.showTick ? this.axisConfig.tickLength : 0) - (this.showAxisLine ? this.axisConfig.axisLineWidth : 0),
        y: this.getScaleValue(i),
        fill: this.axisThemeConfig.labelColor,
        fontSize: this.axisConfig.labelFontSize,
        rotation: 0,
        verticalPos: "middle",
        horizontalPos: "right"
      }))
    }), this.showTick) {
      const i = this.boundingRect.x + this.boundingRect.width - (this.showAxisLine ? this.axisConfig.axisLineWidth : 0);
      t.push({
        type: "path",
        groupTexts: ["left-axis", "ticks"],
        data: this.getTickValues().map((s) => ({
          path: `M ${i},${this.getScaleValue(s)} L ${i - this.axisConfig.tickLength},${this.getScaleValue(s)}`,
          strokeFill: this.axisThemeConfig.tickColor,
          strokeWidth: this.axisConfig.tickWidth
        }))
      });
    }
    return this.showTitle && t.push({
      type: "text",
      groupTexts: ["left-axis", "title"],
      data: [
        {
          text: this.title,
          x: this.boundingRect.x + this.axisConfig.titlePadding,
          y: this.boundingRect.y + this.boundingRect.height / 2,
          fill: this.axisThemeConfig.titleColor,
          fontSize: this.axisConfig.titleFontSize,
          rotation: 270,
          verticalPos: "top",
          horizontalPos: "center"
        }
      ]
    }), t;
  }
  getDrawableElementsForBottomAxis() {
    const t = [];
    if (this.showAxisLine) {
      const i = this.boundingRect.y + this.axisConfig.axisLineWidth / 2;
      t.push({
        type: "path",
        groupTexts: ["bottom-axis", "axis-line"],
        data: [
          {
            path: `M ${this.boundingRect.x},${i} L ${this.boundingRect.x + this.boundingRect.width},${i}`,
            strokeFill: this.axisThemeConfig.axisLineColor,
            strokeWidth: this.axisConfig.axisLineWidth
          }
        ]
      });
    }
    if (this.showLabel && t.push({
      type: "text",
      groupTexts: ["bottom-axis", "label"],
      data: this.getTickValues().map((i) => ({
        text: i.toString(),
        x: this.getScaleValue(i),
        y: this.boundingRect.y + this.axisConfig.labelPadding + (this.showTick ? this.axisConfig.tickLength : 0) + (this.showAxisLine ? this.axisConfig.axisLineWidth : 0),
        fill: this.axisThemeConfig.labelColor,
        fontSize: this.axisConfig.labelFontSize,
        rotation: 0,
        verticalPos: "top",
        horizontalPos: "center"
      }))
    }), this.showTick) {
      const i = this.boundingRect.y + (this.showAxisLine ? this.axisConfig.axisLineWidth : 0);
      t.push({
        type: "path",
        groupTexts: ["bottom-axis", "ticks"],
        data: this.getTickValues().map((s) => ({
          path: `M ${this.getScaleValue(s)},${i} L ${this.getScaleValue(s)},${i + this.axisConfig.tickLength}`,
          strokeFill: this.axisThemeConfig.tickColor,
          strokeWidth: this.axisConfig.tickWidth
        }))
      });
    }
    return this.showTitle && t.push({
      type: "text",
      groupTexts: ["bottom-axis", "title"],
      data: [
        {
          text: this.title,
          x: this.range[0] + (this.range[1] - this.range[0]) / 2,
          y: this.boundingRect.y + this.boundingRect.height - this.axisConfig.titlePadding - this.titleTextHeight,
          fill: this.axisThemeConfig.titleColor,
          fontSize: this.axisConfig.titleFontSize,
          rotation: 0,
          verticalPos: "top",
          horizontalPos: "center"
        }
      ]
    }), t;
  }
  getDrawableElementsForTopAxis() {
    const t = [];
    if (this.showAxisLine) {
      const i = this.boundingRect.y + this.boundingRect.height - this.axisConfig.axisLineWidth / 2;
      t.push({
        type: "path",
        groupTexts: ["top-axis", "axis-line"],
        data: [
          {
            path: `M ${this.boundingRect.x},${i} L ${this.boundingRect.x + this.boundingRect.width},${i}`,
            strokeFill: this.axisThemeConfig.axisLineColor,
            strokeWidth: this.axisConfig.axisLineWidth
          }
        ]
      });
    }
    if (this.showLabel && t.push({
      type: "text",
      groupTexts: ["top-axis", "label"],
      data: this.getTickValues().map((i) => ({
        text: i.toString(),
        x: this.getScaleValue(i),
        y: this.boundingRect.y + (this.showTitle ? this.titleTextHeight + this.axisConfig.titlePadding * 2 : 0) + this.axisConfig.labelPadding,
        fill: this.axisThemeConfig.labelColor,
        fontSize: this.axisConfig.labelFontSize,
        rotation: 0,
        verticalPos: "top",
        horizontalPos: "center"
      }))
    }), this.showTick) {
      const i = this.boundingRect.y;
      t.push({
        type: "path",
        groupTexts: ["top-axis", "ticks"],
        data: this.getTickValues().map((s) => ({
          path: `M ${this.getScaleValue(s)},${i + this.boundingRect.height - (this.showAxisLine ? this.axisConfig.axisLineWidth : 0)} L ${this.getScaleValue(s)},${i + this.boundingRect.height - this.axisConfig.tickLength - (this.showAxisLine ? this.axisConfig.axisLineWidth : 0)}`,
          strokeFill: this.axisThemeConfig.tickColor,
          strokeWidth: this.axisConfig.tickWidth
        }))
      });
    }
    return this.showTitle && t.push({
      type: "text",
      groupTexts: ["top-axis", "title"],
      data: [
        {
          text: this.title,
          x: this.boundingRect.x + this.boundingRect.width / 2,
          y: this.boundingRect.y + this.axisConfig.titlePadding,
          fill: this.axisThemeConfig.titleColor,
          fontSize: this.axisConfig.titleFontSize,
          rotation: 0,
          verticalPos: "top",
          horizontalPos: "center"
        }
      ]
    }), t;
  }
  getDrawableElements() {
    if (this.axisPosition === "left")
      return this.getDrawableElementsForLeftAxis();
    if (this.axisPosition === "right")
      throw Error("Drawing of right axis is not implemented");
    return this.axisPosition === "bottom" ? this.getDrawableElementsForBottomAxis() : this.axisPosition === "top" ? this.getDrawableElementsForTopAxis() : [];
  }
}
class ii extends Rt {
  constructor(t, i, s, n, o) {
    super(t, n, o, i), this.categories = s, this.scale = st().domain(this.categories).range(this.getRange());
  }
  setRange(t) {
    super.setRange(t);
  }
  recalculateScale() {
    this.scale = st().domain(this.categories).range(this.getRange()).paddingInner(1).paddingOuter(0).align(0.5), wt.trace("BandAxis axis final categories, range: ", this.categories, this.getRange());
  }
  getTickValues() {
    return this.categories;
  }
  getScaleValue(t) {
    return this.scale(t) || this.getRange()[0];
  }
}
class ei extends Rt {
  constructor(t, i, s, n, o) {
    super(t, n, o, i), this.domain = s, this.scale = ft().domain(this.domain).range(this.getRange());
  }
  getTickValues() {
    return this.scale.ticks();
  }
  recalculateScale() {
    const t = [...this.domain];
    this.axisPosition === "left" && t.reverse(), this.scale = ft().domain(t).range(this.getRange());
  }
  getScaleValue(t) {
    return this.scale(t);
  }
}
function At(e, t, i, s) {
  const n = new kt(s);
  return _t(e) ? new ii(
    t,
    i,
    e.categories,
    e.title,
    n
  ) : new ei(
    t,
    i,
    [e.min, e.max],
    e.title,
    n
  );
}
class si {
  constructor(t, i, s, n) {
    this.textDimensionCalculator = t, this.chartConfig = i, this.chartData = s, this.chartThemeConfig = n, this.boundingRect = {
      x: 0,
      y: 0,
      width: 0,
      height: 0
    }, this.showChartTitle = !1;
  }
  setBoundingBoxXY(t) {
    this.boundingRect.x = t.x, this.boundingRect.y = t.y;
  }
  calculateSpace(t) {
    const i = this.textDimensionCalculator.getMaxDimension(
      [this.chartData.title],
      this.chartConfig.titleFontSize
    ), s = Math.max(i.width, t.width), n = i.height + 2 * this.chartConfig.titlePadding;
    return i.width <= s && i.height <= n && this.chartConfig.showTitle && this.chartData.title && (this.boundingRect.width = s, this.boundingRect.height = n, this.showChartTitle = !0), {
      width: this.boundingRect.width,
      height: this.boundingRect.height
    };
  }
  getDrawableElements() {
    const t = [];
    return this.showChartTitle && t.push({
      groupTexts: ["chart-title"],
      type: "text",
      data: [
        {
          fontSize: this.chartConfig.titleFontSize,
          text: this.chartData.title,
          verticalPos: "middle",
          horizontalPos: "center",
          x: this.boundingRect.x + this.boundingRect.width / 2,
          y: this.boundingRect.y + this.boundingRect.height / 2,
          fill: this.chartThemeConfig.titleColor,
          rotation: 0
        }
      ]
    }), t;
  }
}
function ni(e, t, i, s) {
  const n = new kt(s);
  return new si(n, e, t, i);
}
class ai {
  constructor(t, i, s, n, o) {
    this.plotData = t, this.xAxis = i, this.yAxis = s, this.orientation = n, this.plotIndex = o;
  }
  getDrawableElement() {
    const t = this.plotData.data.map((s) => [
      this.xAxis.getScaleValue(s[0]),
      this.yAxis.getScaleValue(s[1])
    ]);
    let i;
    return this.orientation === "horizontal" ? i = pt().y((s) => s[0]).x((s) => s[1])(t) : i = pt().x((s) => s[0]).y((s) => s[1])(t), i ? [
      {
        groupTexts: ["plot", `line-plot-${this.plotIndex}`],
        type: "path",
        data: [
          {
            path: i,
            strokeFill: this.plotData.strokeFill,
            strokeWidth: this.plotData.strokeWidth
          }
        ]
      }
    ] : [];
  }
}
class oi {
  constructor(t, i, s, n, o, c) {
    this.barData = t, this.boundingRect = i, this.xAxis = s, this.yAxis = n, this.orientation = o, this.plotIndex = c;
  }
  getDrawableElement() {
    const t = this.barData.data.map((o) => [
      this.xAxis.getScaleValue(o[0]),
      this.yAxis.getScaleValue(o[1])
    ]), i = 0.05, s = Math.min(this.xAxis.getAxisOuterPadding() * 2, this.xAxis.getTickDistance()) * (1 - i), n = s / 2;
    return this.orientation === "horizontal" ? [
      {
        groupTexts: ["plot", `bar-plot-${this.plotIndex}`],
        type: "rect",
        data: t.map((o) => ({
          x: this.boundingRect.x,
          y: o[0] - n,
          height: s,
          width: o[1] - this.boundingRect.x,
          fill: this.barData.fill,
          strokeWidth: 0,
          strokeFill: this.barData.fill
        }))
      }
    ] : [
      {
        groupTexts: ["plot", `bar-plot-${this.plotIndex}`],
        type: "rect",
        data: t.map((o) => ({
          x: o[0] - n,
          y: o[1],
          width: s,
          height: this.boundingRect.y + this.boundingRect.height - o[1],
          fill: this.barData.fill,
          strokeWidth: 0,
          strokeFill: this.barData.fill
        }))
      }
    ];
  }
}
class ri {
  constructor(t, i, s) {
    this.chartConfig = t, this.chartData = i, this.chartThemeConfig = s, this.boundingRect = {
      x: 0,
      y: 0,
      width: 0,
      height: 0
    };
  }
  setAxes(t, i) {
    this.xAxis = t, this.yAxis = i;
  }
  setBoundingBoxXY(t) {
    this.boundingRect.x = t.x, this.boundingRect.y = t.y;
  }
  calculateSpace(t) {
    return this.boundingRect.width = t.width, this.boundingRect.height = t.height, {
      width: this.boundingRect.width,
      height: this.boundingRect.height
    };
  }
  getDrawableElements() {
    if (!(this.xAxis && this.yAxis))
      throw Error("Axes must be passed to render Plots");
    const t = [];
    for (const [i, s] of this.chartData.plots.entries())
      switch (s.type) {
        case "line":
          {
            const n = new ai(
              s,
              this.xAxis,
              this.yAxis,
              this.chartConfig.chartOrientation,
              i
            );
            t.push(...n.getDrawableElement());
          }
          break;
        case "bar":
          {
            const n = new oi(
              s,
              this.boundingRect,
              this.xAxis,
              this.yAxis,
              this.chartConfig.chartOrientation,
              i
            );
            t.push(...n.getDrawableElement());
          }
          break;
      }
    return t;
  }
}
function hi(e, t, i) {
  return new ri(e, t, i);
}
class li {
  constructor(t, i, s, n) {
    this.chartConfig = t, this.chartData = i, this.componentStore = {
      title: ni(t, i, s, n),
      plot: hi(t, i, s),
      xAxis: At(
        i.xAxis,
        t.xAxis,
        {
          titleColor: s.xAxisTitleColor,
          labelColor: s.xAxisLabelColor,
          tickColor: s.xAxisTickColor,
          axisLineColor: s.xAxisLineColor
        },
        n
      ),
      yAxis: At(
        i.yAxis,
        t.yAxis,
        {
          titleColor: s.yAxisTitleColor,
          labelColor: s.yAxisLabelColor,
          tickColor: s.yAxisTickColor,
          axisLineColor: s.yAxisLineColor
        },
        n
      )
    };
  }
  calculateVerticalSpace() {
    let t = this.chartConfig.width, i = this.chartConfig.height, s = 0, n = 0, o = Math.floor(t * this.chartConfig.plotReservedSpacePercent / 100), c = Math.floor(
      i * this.chartConfig.plotReservedSpacePercent / 100
    ), f = this.componentStore.plot.calculateSpace({
      width: o,
      height: c
    });
    t -= f.width, i -= f.height, f = this.componentStore.title.calculateSpace({
      width: this.chartConfig.width,
      height: i
    }), n = f.height, i -= f.height, this.componentStore.xAxis.setAxisPosition("bottom"), f = this.componentStore.xAxis.calculateSpace({
      width: t,
      height: i
    }), i -= f.height, this.componentStore.yAxis.setAxisPosition("left"), f = this.componentStore.yAxis.calculateSpace({
      width: t,
      height: i
    }), s = f.width, t -= f.width, t > 0 && (o += t, t = 0), i > 0 && (c += i, i = 0), this.componentStore.plot.calculateSpace({
      width: o,
      height: c
    }), this.componentStore.plot.setBoundingBoxXY({ x: s, y: n }), this.componentStore.xAxis.setRange([s, s + o]), this.componentStore.xAxis.setBoundingBoxXY({ x: s, y: n + c }), this.componentStore.yAxis.setRange([n, n + c]), this.componentStore.yAxis.setBoundingBoxXY({ x: 0, y: n }), this.chartData.plots.some((d) => mt(d)) && this.componentStore.xAxis.recalculateOuterPaddingToDrawBar();
  }
  calculateHorizonatalSpace() {
    let t = this.chartConfig.width, i = this.chartConfig.height, s = 0, n = 0, o = 0, c = Math.floor(t * this.chartConfig.plotReservedSpacePercent / 100), f = Math.floor(
      i * this.chartConfig.plotReservedSpacePercent / 100
    ), d = this.componentStore.plot.calculateSpace({
      width: c,
      height: f
    });
    t -= d.width, i -= d.height, d = this.componentStore.title.calculateSpace({
      width: this.chartConfig.width,
      height: i
    }), s = d.height, i -= d.height, this.componentStore.xAxis.setAxisPosition("left"), d = this.componentStore.xAxis.calculateSpace({
      width: t,
      height: i
    }), t -= d.width, n = d.width, this.componentStore.yAxis.setAxisPosition("top"), d = this.componentStore.yAxis.calculateSpace({
      width: t,
      height: i
    }), i -= d.height, o = s + d.height, t > 0 && (c += t, t = 0), i > 0 && (f += i, i = 0), this.componentStore.plot.calculateSpace({
      width: c,
      height: f
    }), this.componentStore.plot.setBoundingBoxXY({ x: n, y: o }), this.componentStore.yAxis.setRange([n, n + c]), this.componentStore.yAxis.setBoundingBoxXY({ x: n, y: s }), this.componentStore.xAxis.setRange([o, o + f]), this.componentStore.xAxis.setBoundingBoxXY({ x: 0, y: o }), this.chartData.plots.some((R) => mt(R)) && this.componentStore.xAxis.recalculateOuterPaddingToDrawBar();
  }
  calculateSpace() {
    this.chartConfig.chartOrientation === "horizontal" ? this.calculateHorizonatalSpace() : this.calculateVerticalSpace();
  }
  getDrawableElement() {
    this.calculateSpace();
    const t = [];
    this.componentStore.plot.setAxes(this.componentStore.xAxis, this.componentStore.yAxis);
    for (const i of Object.values(this.componentStore))
      t.push(...i.getDrawableElements());
    return t;
  }
}
class ci {
  static build(t, i, s, n) {
    return new li(t, i, s, n).getDrawableElement();
  }
}
let X = 0, Tt, Y = Pt(), H = Dt(), y = Lt(), at = H.plotColorPalette.split(",").map((e) => e.trim()), G = !1, rt = !1;
function Dt() {
  const e = Ht(), t = ot();
  return Ct(e.xyChart, t.themeVariables.xyChart);
}
function Pt() {
  const e = ot();
  return Ct(
    Ut.xyChart,
    e.xyChart
  );
}
function Lt() {
  return {
    yAxis: {
      type: "linear",
      title: "",
      min: 1 / 0,
      max: -1 / 0
    },
    xAxis: {
      type: "band",
      title: "",
      categories: []
    },
    title: "",
    plots: []
  };
}
function ht(e) {
  const t = ot();
  return qt(e.trim(), t);
}
function ui(e) {
  Tt = e;
}
function gi(e) {
  e === "horizontal" ? Y.chartOrientation = "horizontal" : Y.chartOrientation = "vertical";
}
function xi(e) {
  y.xAxis.title = ht(e.text);
}
function Et(e, t) {
  y.xAxis = { type: "linear", title: y.xAxis.title, min: e, max: t }, G = !0;
}
function di(e) {
  y.xAxis = {
    type: "band",
    title: y.xAxis.title,
    categories: e.map((t) => ht(t.text))
  }, G = !0;
}
function fi(e) {
  y.yAxis.title = ht(e.text);
}
function pi(e, t) {
  y.yAxis = { type: "linear", title: y.yAxis.title, min: e, max: t }, rt = !0;
}
function mi(e) {
  const t = Math.min(...e), i = Math.max(...e), s = N(y.yAxis) ? y.yAxis.min : 1 / 0, n = N(y.yAxis) ? y.yAxis.max : -1 / 0;
  y.yAxis = {
    type: "linear",
    title: y.yAxis.title,
    min: Math.min(s, t),
    max: Math.max(n, i)
  };
}
function vt(e) {
  let t = [];
  if (e.length === 0)
    return t;
  if (!G) {
    const i = N(y.xAxis) ? y.xAxis.min : 1 / 0, s = N(y.xAxis) ? y.xAxis.max : -1 / 0;
    Et(Math.min(i, 1), Math.max(s, e.length));
  }
  if (rt || mi(e), _t(y.xAxis) && (t = y.xAxis.categories.map((i, s) => [i, e[s]])), N(y.xAxis)) {
    const i = y.xAxis.min, s = y.xAxis.max, n = (s - i + 1) / e.length, o = [];
    for (let c = i; c <= s; c += n)
      o.push(`${c}`);
    t = o.map((c, f) => [c, e[f]]);
  }
  return t;
}
function Mt(e) {
  return at[e === 0 ? 0 : e % at.length];
}
function yi(e, t) {
  const i = vt(t);
  y.plots.push({
    type: "line",
    strokeFill: Mt(X),
    strokeWidth: 2,
    data: i
  }), X++;
}
function bi(e, t) {
  const i = vt(t);
  y.plots.push({
    type: "bar",
    fill: Mt(X),
    data: i
  }), X++;
}
function Ai() {
  if (y.plots.length === 0)
    throw Error("No Plot to render, please provide a plot with some data");
  return y.title = St(), ci.build(Y, y, H, Tt);
}
function wi() {
  return H;
}
function Si() {
  return Y;
}
const Ci = function() {
  $t(), X = 0, Y = Pt(), y = Lt(), H = Dt(), at = H.plotColorPalette.split(",").map((e) => e.trim()), G = !1, rt = !1;
}, _i = {
  getDrawableElem: Ai,
  clear: Ci,
  setAccTitle: zt,
  getAccTitle: Ft,
  setDiagramTitle: Nt,
  getDiagramTitle: St,
  getAccDescription: Xt,
  setAccDescription: Yt,
  setOrientation: gi,
  setXAxisTitle: xi,
  setXAxisRangeData: Et,
  setXAxisBand: di,
  setYAxisTitle: fi,
  setYAxisRangeData: pi,
  setLineData: yi,
  setBarData: bi,
  setTmpSVGG: ui,
  getChartThemeConfig: wi,
  getChartConfig: Si
}, ki = (e, t, i, s) => {
  const n = s.db, o = n.getChartThemeConfig(), c = n.getChartConfig();
  function f(p) {
    return p === "top" ? "text-before-edge" : "middle";
  }
  function d(p) {
    return p === "left" ? "start" : p === "right" ? "end" : "middle";
  }
  function R(p) {
    return `translate(${p.x}, ${p.y}) rotate(${p.rotation || 0})`;
  }
  wt.debug(`Rendering xychart chart
` + e);
  const _ = jt(t), A = _.append("g").attr("class", "main"), m = A.append("rect").attr("width", c.width).attr("height", c.height).attr("class", "background");
  Gt(_, c.height, c.width, !0), _.attr("viewBox", `0 0 ${c.width} ${c.height}`), m.attr("fill", o.backgroundColor), n.setTmpSVGG(_.append("g").attr("class", "mermaid-tmp-group"));
  const T = n.getDrawableElem(), S = {};
  function P(p) {
    let C = A, h = "";
    for (const [L] of p.entries()) {
      let z = A;
      L > 0 && S[h] && (z = S[h]), h += p[L], C = S[h], C || (C = S[h] = z.append("g").attr("class", p[L]));
    }
    return C;
  }
  for (const p of T) {
    if (p.data.length === 0)
      continue;
    const C = P(p.groupTexts);
    switch (p.type) {
      case "rect":
        C.selectAll("rect").data(p.data).enter().append("rect").attr("x", (h) => h.x).attr("y", (h) => h.y).attr("width", (h) => h.width).attr("height", (h) => h.height).attr("fill", (h) => h.fill).attr("stroke", (h) => h.strokeFill).attr("stroke-width", (h) => h.strokeWidth);
        break;
      case "text":
        C.selectAll("text").data(p.data).enter().append("text").attr("x", 0).attr("y", 0).attr("fill", (h) => h.fill).attr("font-size", (h) => h.fontSize).attr("dominant-baseline", (h) => f(h.verticalPos)).attr("text-anchor", (h) => d(h.horizontalPos)).attr("transform", (h) => R(h)).text((h) => h.text);
        break;
      case "path":
        C.selectAll("path").data(p.data).enter().append("path").attr("d", (h) => h.path).attr("fill", (h) => h.fill ? h.fill : "none").attr("stroke", (h) => h.strokeFill).attr("stroke-width", (h) => h.strokeWidth);
        break;
    }
  }
}, Ri = {
  draw: ki
}, Vi = {
  parser: ti,
  db: _i,
  renderer: Ri
};
export {
  Vi as diagram
};
