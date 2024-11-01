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
  claim_component: w,
  create_component: g,
  create_slot: h,
  destroy_component: k,
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
  mount_component: F,
  noop: a,
  safe_not_equal: I,
  transition_in: u,
  transition_out: _,
  update_await_block_branch: N,
  update_slot_base: S
} = window.__gradio__svelte__internal;
function A(l) {
  return {
    c: a,
    l: a,
    m: a,
    p: a,
    i: a,
    o: a,
    d: a
  };
}
function B(l) {
  let t, i;
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
  return t = new /*Flow*/
  l[5]({
    props: o
  }), {
    c() {
      g(t.$$.fragment);
    },
    l(n) {
      w(t.$$.fragment, n);
    },
    m(n, r) {
      F(t, n, r), i = !0;
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
      i || (u(t.$$.fragment, n), i = !0);
    },
    o(n) {
      _(t.$$.fragment, n), i = !1;
    },
    d(n) {
      k(t, n);
    }
  };
}
function D(l) {
  let t;
  const i = (
    /*#slots*/
    l[2].default
  ), e = h(
    i,
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
        i,
        o,
        /*$$scope*/
        o[3],
        t ? P(
          i,
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
    c: a,
    l: a,
    m: a,
    p: a,
    i: a,
    o: a,
    d: a
  };
}
function G(l) {
  let t, i, e = {
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
    /*awaitedFlow*/
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
      q(o, t, n), e.block.m(o, e.anchor = n), e.mount = () => t.parentNode, e.anchor = t, i = !0;
    },
    p(o, [n]) {
      l = o, N(e, l, n);
    },
    i(o) {
      i || (u(e.block), i = !0);
    },
    o(o) {
      for (let n = 0; n < 3; n += 1) {
        const r = e.blocks[n];
        _(r);
      }
      i = !1;
    },
    d(o) {
      o && $(t), e.block.d(o), e.token = null, e = null;
    }
  };
}
function H(l, t, i) {
  let e, {
    $$slots: o = {},
    $$scope: n
  } = t;
  const r = p(() => import("./Awaited-BmJwijJt.js"));
  return l.$$set = (c) => {
    i(4, t = s(s({}, t), m(c))), "$$scope" in c && i(3, n = c.$$scope);
  }, l.$$.update = () => {
    i(0, e = t);
  }, t = m(t), [e, r, o, n];
}
class J extends b {
  constructor(t) {
    super(), j(this, t, H, G, I, {});
  }
}
export {
  J as default
};
