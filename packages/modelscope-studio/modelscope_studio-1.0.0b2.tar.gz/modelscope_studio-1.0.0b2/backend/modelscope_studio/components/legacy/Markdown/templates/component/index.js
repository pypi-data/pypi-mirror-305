async function d() {
  window.ms_globals.initializePromise || (window.ms_globals.initializePromise = new Promise((l) => {
    window.ms_globals.initialize = () => {
      l();
    };
  })), await window.ms_globals.initializePromise;
}
async function p(l) {
  return await d(), l().then((t) => t.default);
}
const {
  SvelteComponent: b,
  assign: s,
  claim_component: k,
  create_component: w,
  create_slot: g,
  destroy_component: h,
  detach: $,
  empty: f,
  exclude_internal_props: m,
  get_all_dirty_from_scope: z,
  get_slot_changes: P,
  get_spread_object: y,
  get_spread_update: C,
  handle_promise: v,
  init: j,
  insert_hydration: q,
  mount_component: I,
  noop: i,
  safe_not_equal: M,
  transition_in: u,
  transition_out: _,
  update_await_block_branch: N,
  update_slot_base: S
} = window.__gradio__svelte__internal;
function A(l) {
  return {
    c: i,
    l: i,
    m: i,
    p: i,
    i,
    o: i,
    d: i
  };
}
function B(l) {
  let t, a;
  const e = [
    /*args*/
    l[0]
  ];
  let o = {
    $$slots: {
      default: [D]
    },
    $$scope: {
      ctx: l
    }
  };
  for (let n = 0; n < e.length; n += 1)
    o = s(o, e[n]);
  return t = new /*Markdown*/
  l[5]({
    props: o
  }), {
    c() {
      w(t.$$.fragment);
    },
    l(n) {
      k(t.$$.fragment, n);
    },
    m(n, r) {
      I(t, n, r), a = !0;
    },
    p(n, r) {
      const c = r & /*args*/
      1 ? C(e, [y(
        /*args*/
        n[0]
      )]) : {};
      r & /*$$scope*/
      8 && (c.$$scope = {
        dirty: r,
        ctx: n
      }), t.$set(c);
    },
    i(n) {
      a || (u(t.$$.fragment, n), a = !0);
    },
    o(n) {
      _(t.$$.fragment, n), a = !1;
    },
    d(n) {
      h(t, n);
    }
  };
}
function D(l) {
  let t;
  const a = (
    /*#slots*/
    l[2].default
  ), e = g(
    a,
    l,
    /*$$scope*/
    l[3],
    null
  );
  return {
    c() {
      e && e.c();
    },
    l(o) {
      e && e.l(o);
    },
    m(o, n) {
      e && e.m(o, n), t = !0;
    },
    p(o, n) {
      e && e.p && (!t || n & /*$$scope*/
      8) && S(
        e,
        a,
        o,
        /*$$scope*/
        o[3],
        t ? P(
          a,
          /*$$scope*/
          o[3],
          n,
          null
        ) : z(
          /*$$scope*/
          o[3]
        ),
        null
      );
    },
    i(o) {
      t || (u(e, o), t = !0);
    },
    o(o) {
      _(e, o), t = !1;
    },
    d(o) {
      e && e.d(o);
    }
  };
}
function E(l) {
  return {
    c: i,
    l: i,
    m: i,
    p: i,
    i,
    o: i,
    d: i
  };
}
function F(l) {
  let t, a, e = {
    ctx: l,
    current: null,
    token: null,
    hasCatch: !1,
    pending: E,
    then: B,
    catch: A,
    value: 5,
    blocks: [, , ,]
  };
  return v(
    /*awaitedMarkdown*/
    l[1],
    e
  ), {
    c() {
      t = f(), e.block.c();
    },
    l(o) {
      t = f(), e.block.l(o);
    },
    m(o, n) {
      q(o, t, n), e.block.m(o, e.anchor = n), e.mount = () => t.parentNode, e.anchor = t, a = !0;
    },
    p(o, [n]) {
      l = o, N(e, l, n);
    },
    i(o) {
      a || (u(e.block), a = !0);
    },
    o(o) {
      for (let n = 0; n < 3; n += 1) {
        const r = e.blocks[n];
        _(r);
      }
      a = !1;
    },
    d(o) {
      o && $(t), e.block.d(o), e.token = null, e = null;
    }
  };
}
function G(l, t, a) {
  let e, {
    $$slots: o = {},
    $$scope: n
  } = t;
  const r = p(() => import("./Awaited-DMh-meaP.js"));
  return l.$$set = (c) => {
    a(4, t = s(s({}, t), m(c))), "$$scope" in c && a(3, n = c.$$scope);
  }, l.$$.update = () => {
    a(0, e = t);
  }, t = m(t), [e, r, o, n];
}
class H extends b {
  constructor(t) {
    super(), j(this, t, G, F, M, {});
  }
}
export {
  H as default
};
