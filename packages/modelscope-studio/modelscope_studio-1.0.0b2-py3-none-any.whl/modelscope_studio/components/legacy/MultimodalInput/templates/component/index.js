async function d() {
  window.ms_globals.initializePromise || (window.ms_globals.initializePromise = new Promise((o) => {
    window.ms_globals.initialize = () => {
      o();
    };
  })), await window.ms_globals.initializePromise;
}
async function p(o) {
  return await d(), o().then((e) => e.default);
}
const {
  SvelteComponent: b,
  assign: s,
  claim_component: g,
  create_component: h,
  create_slot: k,
  destroy_component: w,
  detach: $,
  empty: m,
  exclude_internal_props: f,
  get_all_dirty_from_scope: z,
  get_slot_changes: P,
  get_spread_object: y,
  get_spread_update: C,
  handle_promise: v,
  init: I,
  insert_hydration: j,
  mount_component: q,
  noop: a,
  safe_not_equal: M,
  transition_in: u,
  transition_out: _,
  update_await_block_branch: N,
  update_slot_base: S
} = window.__gradio__svelte__internal;
function A(o) {
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
function B(o) {
  let e, i;
  const t = [
    /*args*/
    o[0]
  ];
  let l = {
    $$slots: {
      default: [D]
    },
    $$scope: {
      ctx: o
    }
  };
  for (let n = 0; n < t.length; n += 1)
    l = s(l, t[n]);
  return e = new /*MultimodalInput*/
  o[5]({
    props: l
  }), {
    c() {
      h(e.$$.fragment);
    },
    l(n) {
      g(e.$$.fragment, n);
    },
    m(n, r) {
      q(e, n, r), i = !0;
    },
    p(n, r) {
      const c = r & /*args*/
      1 ? C(t, [y(
        /*args*/
        n[0]
      )]) : {};
      r & /*$$scope*/
      8 && (c.$$scope = {
        dirty: r,
        ctx: n
      }), e.$set(c);
    },
    i(n) {
      i || (u(e.$$.fragment, n), i = !0);
    },
    o(n) {
      _(e.$$.fragment, n), i = !1;
    },
    d(n) {
      w(e, n);
    }
  };
}
function D(o) {
  let e;
  const i = (
    /*#slots*/
    o[2].default
  ), t = k(
    i,
    o,
    /*$$scope*/
    o[3],
    null
  );
  return {
    c() {
      t && t.c();
    },
    l(l) {
      t && t.l(l);
    },
    m(l, n) {
      t && t.m(l, n), e = !0;
    },
    p(l, n) {
      t && t.p && (!e || n & /*$$scope*/
      8) && S(
        t,
        i,
        l,
        /*$$scope*/
        l[3],
        e ? P(
          i,
          /*$$scope*/
          l[3],
          n,
          null
        ) : z(
          /*$$scope*/
          l[3]
        ),
        null
      );
    },
    i(l) {
      e || (u(t, l), e = !0);
    },
    o(l) {
      _(t, l), e = !1;
    },
    d(l) {
      t && t.d(l);
    }
  };
}
function E(o) {
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
function F(o) {
  let e, i, t = {
    ctx: o,
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
    /*awaitedMultimodalInput*/
    o[1],
    t
  ), {
    c() {
      e = m(), t.block.c();
    },
    l(l) {
      e = m(), t.block.l(l);
    },
    m(l, n) {
      j(l, e, n), t.block.m(l, t.anchor = n), t.mount = () => e.parentNode, t.anchor = e, i = !0;
    },
    p(l, [n]) {
      o = l, N(t, o, n);
    },
    i(l) {
      i || (u(t.block), i = !0);
    },
    o(l) {
      for (let n = 0; n < 3; n += 1) {
        const r = t.blocks[n];
        _(r);
      }
      i = !1;
    },
    d(l) {
      l && $(e), t.block.d(l), t.token = null, t = null;
    }
  };
}
function G(o, e, i) {
  let t, {
    $$slots: l = {},
    $$scope: n
  } = e;
  const r = p(() => import("./Awaited-DmZ3Tgve.js"));
  return o.$$set = (c) => {
    i(4, e = s(s({}, e), f(c))), "$$scope" in c && i(3, n = c.$$scope);
  }, o.$$.update = () => {
    i(0, t = e);
  }, e = f(e), [t, r, l, n];
}
class H extends b {
  constructor(e) {
    super(), I(this, e, G, F, M, {});
  }
}
export {
  H as default
};
