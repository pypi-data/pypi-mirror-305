const {
  SvelteComponent: Z,
  append: p,
  attr: v,
  destroy_each: E,
  detach: O,
  element: b,
  empty: P,
  ensure_array_like: j,
  flush: F,
  init: x,
  insert: C,
  listen: T,
  noop: B,
  run_all: $,
  safe_not_equal: ee,
  set_data: te,
  set_input_value: ne,
  space: R,
  text: D,
  toggle_class: G
} = window.__gradio__svelte__internal, { tick: H } = window.__gradio__svelte__internal;
function K(t, e, l) {
  const a = t.slice();
  return a[16] = e[l], a;
}
function L(t, e, l) {
  const a = t.slice();
  return a[19] = e[l], a;
}
function le(t) {
  let e, l = (
    /*pageNumber*/
    t[19] + ""
  ), a, c, s;
  function r() {
    return (
      /*click_handler_1*/
      t[11](
        /*pageNumber*/
        t[19]
      )
    );
  }
  return {
    c() {
      e = b("button"), a = D(l), v(e, "class", "page-button svelte-1bca5rq"), G(
        e,
        "selected",
        /*page*/
        t[1] === /*pageNumber*/
        t[19]
      );
    },
    m(u, _) {
      C(u, e, _), p(e, a), c || (s = T(e, "click", r), c = !0);
    },
    p(u, _) {
      t = u, _ & /*page, max_page*/
      6 && l !== (l = /*pageNumber*/
      t[19] + "") && te(a, l), _ & /*page, paginationRange, max_page*/
      6 && G(
        e,
        "selected",
        /*page*/
        t[1] === /*pageNumber*/
        t[19]
      );
    },
    d(u) {
      u && O(e), c = !1, s();
    }
  };
}
function ie(t) {
  let e;
  return {
    c() {
      e = b("span"), e.textContent = "...", v(e, "class", "dots svelte-1bca5rq");
    },
    m(l, a) {
      C(l, e, a);
    },
    p: B,
    d(l) {
      l && O(e);
    }
  };
}
function Q(t) {
  let e;
  function l(s, r) {
    return (
      /*pageNumber*/
      s[19] === "..." ? ie : le
    );
  }
  let a = l(t), c = a(t);
  return {
    c() {
      c.c(), e = P();
    },
    m(s, r) {
      c.m(s, r), C(s, e, r);
    },
    p(s, r) {
      a === (a = l(s)) && c ? c.p(s, r) : (c.d(1), c = a(s), c && (c.c(), c.m(e.parentNode, e)));
    },
    d(s) {
      s && O(e), c.d(s);
    }
  };
}
function U(t) {
  let e, l = (
    /*size*/
    t[16] + ""
  ), a, c, s;
  return {
    c() {
      e = b("option"), a = D(l), c = D(" per page"), e.__value = /*size*/
      t[16], ne(e, e.__value), e.selected = s = /*size*/
      t[16] === /*page_size*/
      t[0];
    },
    m(r, u) {
      C(r, e, u), p(e, a), p(e, c);
    },
    p(r, u) {
      u & /*page_size*/
      1 && s !== (s = /*size*/
      r[16] === /*page_size*/
      r[0]) && (e.selected = s);
    },
    d(r) {
      r && O(e);
    }
  };
}
function se(t) {
  let e, l, a, c, s, r, u, _, d, z, m, N, g, S, I, k = j(W(
    /*page*/
    t[1],
    /*max_page*/
    t[2]
  )), f = [];
  for (let n = 0; n < k.length; n += 1)
    f[n] = Q(L(t, k, n));
  let w = j(
    /*page_size_options*/
    t[4]
  ), o = [];
  for (let n = 0; n < w.length; n += 1)
    o[n] = U(K(t, w, n));
  return {
    c() {
      e = b("div"), l = b("span"), l.textContent = `Total ${/*total*/
      t[3]} Items`, a = R(), c = b("button"), s = b("div"), u = R();
      for (let n = 0; n < f.length; n += 1)
        f[n].c();
      _ = R(), d = b("button"), z = b("div"), N = R(), g = b("select");
      for (let n = 0; n < o.length; n += 1)
        o[n].c();
      v(l, "class", "total svelte-1bca5rq"), v(s, "class", "arrow-prev svelte-1bca5rq"), v(c, "class", "nav-button svelte-1bca5rq"), c.disabled = r = /*page*/
      t[1] === 1, v(z, "class", "arrow-next svelte-1bca5rq"), v(d, "class", "nav-button svelte-1bca5rq"), d.disabled = m = /*page*/
      t[1] === /*max_page*/
      t[2], v(g, "class", "page-size-selector svelte-1bca5rq"), v(e, "class", "pagination svelte-1bca5rq");
    },
    m(n, h) {
      C(n, e, h), p(e, l), p(e, a), p(e, c), p(c, s), p(e, u);
      for (let i = 0; i < f.length; i += 1)
        f[i] && f[i].m(e, null);
      p(e, _), p(e, d), p(d, z), p(e, N), p(e, g);
      for (let i = 0; i < o.length; i += 1)
        o[i] && o[i].m(g, null);
      S || (I = [
        T(
          c,
          "click",
          /*click_handler*/
          t[10]
        ),
        T(
          d,
          "click",
          /*click_handler_2*/
          t[12]
        ),
        T(
          g,
          "change",
          /*handle_page_size_change*/
          t[7]
        )
      ], S = !0);
    },
    p(n, [h]) {
      if (h & /*page*/
      2 && r !== (r = /*page*/
      n[1] === 1) && (c.disabled = r), h & /*paginationRange, page, max_page, handle_page_click, Number*/
      38) {
        k = j(W(
          /*page*/
          n[1],
          /*max_page*/
          n[2]
        ));
        let i;
        for (i = 0; i < k.length; i += 1) {
          const y = L(n, k, i);
          f[i] ? f[i].p(y, h) : (f[i] = Q(y), f[i].c(), f[i].m(e, _));
        }
        for (; i < f.length; i += 1)
          f[i].d(1);
        f.length = k.length;
      }
      if (h & /*page, max_page*/
      6 && m !== (m = /*page*/
      n[1] === /*max_page*/
      n[2]) && (d.disabled = m), h & /*page_size_options, page_size*/
      17) {
        w = j(
          /*page_size_options*/
          n[4]
        );
        let i;
        for (i = 0; i < w.length; i += 1) {
          const y = K(n, w, i);
          o[i] ? o[i].p(y, h) : (o[i] = U(y), o[i].c(), o[i].m(g, null));
        }
        for (; i < o.length; i += 1)
          o[i].d(1);
        o.length = w.length;
      }
    },
    i: B,
    o: B,
    d(n) {
      n && O(e), E(f, n), E(o, n), S = !1, $(I);
    }
  };
}
function W(t, e) {
  const l = [], c = Math.max(2, t - 2), s = Math.min(e - 1, t + 2);
  c > 2 ? l.push(1, "...") : l.push(1);
  for (let r = c; r <= s; r++)
    l.push(r);
  return s < e - 1 ? l.push("...", e) : s === e - 1 && l.push(e), l;
}
function oe(t, e, l) {
  var a = this && this.__awaiter || function(o, n, h, i) {
    function y(J) {
      return J instanceof h ? J : new h(function(M) {
        M(J);
      });
    }
    return new (h || (h = Promise))(function(J, M) {
      function X(q) {
        try {
          V(i.next(q));
        } catch (A) {
          M(A);
        }
      }
      function Y(q) {
        try {
          V(i.throw(q));
        } catch (A) {
          M(A);
        }
      }
      function V(q) {
        q.done ? J(q.value) : y(q.value).then(X, Y);
      }
      V((i = i.apply(o, n || [])).next());
    });
  };
  let { gradio: c } = e, { value: s = "" } = e;
  const r = (o) => {
    try {
      return JSON.parse(o || "{}");
    } catch (n) {
      return console.log(n), { total: 0, page: 1, page_size: 10 };
    }
  };
  let { total: u = 0, page: _ = 1, page_size: d = 10 } = r(s);
  const z = [10, 20, 50, 100];
  let m;
  function N(o) {
    o !== _ && (l(1, _ = o), l(8, s = JSON.stringify({ total: u, page: _, page_size: d })));
  }
  function g(o) {
    const n = _ + o;
    n >= 1 && n <= m && (l(1, _ = n), l(8, s = JSON.stringify({ total: u, page: _, page_size: d })));
  }
  function S(o) {
    return a(this, void 0, void 0, function* () {
      const n = parseInt(o.target.value);
      n !== d && (l(0, d = n), l(1, _ = 1), yield H(), l(8, s = JSON.stringify({ total: u, page: _, page_size: d })));
    });
  }
  function I() {
    return a(this, void 0, void 0, function* () {
      yield H(), c.dispatch("change");
    });
  }
  const k = () => g(-1), f = (o) => N(Number(o)), w = () => g(1);
  return t.$$set = (o) => {
    "gradio" in o && l(9, c = o.gradio), "value" in o && l(8, s = o.value);
  }, t.$$.update = () => {
    t.$$.dirty & /*page_size*/
    1 && l(2, m = Math.ceil(u / d)), t.$$.dirty & /*value*/
    256 && I();
  }, [
    d,
    _,
    m,
    u,
    z,
    N,
    g,
    S,
    s,
    c,
    k,
    f,
    w
  ];
}
class ce extends Z {
  constructor(e) {
    super(), x(this, e, oe, se, ee, { gradio: 9, value: 8 });
  }
  get gradio() {
    return this.$$.ctx[9];
  }
  set gradio(e) {
    this.$$set({ gradio: e }), F();
  }
  get value() {
    return this.$$.ctx[8];
  }
  set value(e) {
    this.$$set({ value: e }), F();
  }
}
export {
  ce as default
};
