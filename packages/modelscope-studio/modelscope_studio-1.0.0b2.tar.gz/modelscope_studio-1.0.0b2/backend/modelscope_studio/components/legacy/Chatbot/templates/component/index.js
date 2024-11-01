async function d() {
  window.ms_globals.initializePromise || (window.ms_globals.initializePromise = new Promise((l) => {
    window.ms_globals.initialize = () => {
      l();
    };
  })), await window.ms_globals.initializePromise;
}
async function p(l) {
  return await d(), l().then((e) => e.default);
}
const {
  SvelteComponent: b,
  assign: s,
  claim_component: h,
  create_component: g,
  create_slot: k,
  destroy_component: w,
  detach: $,
  empty: f,
  exclude_internal_props: m,
  get_all_dirty_from_scope: z,
  get_slot_changes: C,
  get_spread_object: P,
  get_spread_update: y,
  handle_promise: v,
  init: j,
  insert_hydration: q,
  mount_component: I,
  noop: i,
  safe_not_equal: N,
  transition_in: u,
  transition_out: _,
  update_await_block_branch: S,
  update_slot_base: A
} = window.__gradio__svelte__internal;
function B(l) {
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
function D(l) {
  let e, a;
  const t = [
    /*args*/
    l[0]
  ];
  let o = {
    $$slots: {
      default: [E]
    },
    $$scope: {
      ctx: l
    }
  };
  for (let n = 0; n < t.length; n += 1)
    o = s(o, t[n]);
  return e = new /*Chatbot*/
  l[5]({
    props: o
  }), {
    c() {
      g(e.$$.fragment);
    },
    l(n) {
      h(e.$$.fragment, n);
    },
    m(n, c) {
      I(e, n, c), a = !0;
    },
    p(n, c) {
      const r = c & /*args*/
      1 ? y(t, [P(
        /*args*/
        n[0]
      )]) : {};
      c & /*$$scope*/
      8 && (r.$$scope = {
        dirty: c,
        ctx: n
      }), e.$set(r);
    },
    i(n) {
      a || (u(e.$$.fragment, n), a = !0);
    },
    o(n) {
      _(e.$$.fragment, n), a = !1;
    },
    d(n) {
      w(e, n);
    }
  };
}
function E(l) {
  let e;
  const a = (
    /*#slots*/
    l[2].default
  ), t = k(
    a,
    l,
    /*$$scope*/
    l[3],
    null
  );
  return {
    c() {
      t && t.c();
    },
    l(o) {
      t && t.l(o);
    },
    m(o, n) {
      t && t.m(o, n), e = !0;
    },
    p(o, n) {
      t && t.p && (!e || n & /*$$scope*/
      8) && A(
        t,
        a,
        o,
        /*$$scope*/
        o[3],
        e ? C(
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
      e || (u(t, o), e = !0);
    },
    o(o) {
      _(t, o), e = !1;
    },
    d(o) {
      t && t.d(o);
    }
  };
}
function F(l) {
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
function G(l) {
  let e, a, t = {
    ctx: l,
    current: null,
    token: null,
    hasCatch: !1,
    pending: F,
    then: D,
    catch: B,
    value: 5,
    blocks: [, , ,]
  };
  return v(
    /*awaitedChatbot*/
    l[1],
    t
  ), {
    c() {
      e = f(), t.block.c();
    },
    l(o) {
      e = f(), t.block.l(o);
    },
    m(o, n) {
      q(o, e, n), t.block.m(o, t.anchor = n), t.mount = () => e.parentNode, t.anchor = e, a = !0;
    },
    p(o, [n]) {
      l = o, S(t, l, n);
    },
    i(o) {
      a || (u(t.block), a = !0);
    },
    o(o) {
      for (let n = 0; n < 3; n += 1) {
        const c = t.blocks[n];
        _(c);
      }
      a = !1;
    },
    d(o) {
      o && $(e), t.block.d(o), t.token = null, t = null;
    }
  };
}
function H(l, e, a) {
  let t, {
    $$slots: o = {},
    $$scope: n
  } = e;
  const c = p(() => import("./Awaited-CC4Hf28p.js"));
  return l.$$set = (r) => {
    a(4, e = s(s({}, e), m(r))), "$$scope" in r && a(3, n = r.$$scope);
  }, l.$$.update = () => {
    a(0, t = e);
  }, e = m(e), [t, c, o, n];
}
class J extends b {
  constructor(e) {
    super(), j(this, e, H, G, N, {});
  }
}
export {
  J as default
};
