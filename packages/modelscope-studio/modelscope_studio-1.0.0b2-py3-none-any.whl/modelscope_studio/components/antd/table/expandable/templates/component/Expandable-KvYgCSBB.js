import { g as J, b as L } from "./Index-DR5M0ulA.js";
function K() {
}
function Q(t, e) {
  return t != t ? e == e : t !== e || t && typeof t == "object" || typeof t == "function";
}
function U(t, ...e) {
  if (t == null) {
    for (const s of e)
      s(void 0);
    return K;
  }
  const r = t.subscribe(...e);
  return r.unsubscribe ? () => r.unsubscribe() : r;
}
function g(t) {
  let e;
  return U(t, (r) => e = r)(), e;
}
const x = [];
function _(t, e = K) {
  let r;
  const s = /* @__PURE__ */ new Set();
  function o(c) {
    if (Q(t, c) && (t = c, r)) {
      const f = !x.length;
      for (const a of s)
        a[1](), x.push(a, t);
      if (f) {
        for (let a = 0; a < x.length; a += 2)
          x[a][0](x[a + 1]);
        x.length = 0;
      }
    }
  }
  function n(c) {
    o(c(t));
  }
  function i(c, f = K) {
    const a = [c, f];
    return s.add(a), s.size === 1 && (r = e(o, n) || K), c(t), () => {
      s.delete(a), s.size === 0 && r && (r(), r = null);
    };
  }
  return {
    set: o,
    update: n,
    subscribe: i
  };
}
const {
  getContext: V,
  setContext: w
} = window.__gradio__svelte__internal, W = "$$ms-gr-slots-key";
function X() {
  const t = _({});
  return w(W, t);
}
const Y = "$$ms-gr-render-slot-context-key";
function Z() {
  const t = w(Y, _({}));
  return (e, r) => {
    t.update((s) => typeof r == "function" ? {
      ...s,
      [e]: r(s[e])
    } : {
      ...s,
      [e]: r
    });
  };
}
const $ = "$$ms-gr-context-key";
function ee(t, e, r) {
  var d;
  if (!Reflect.has(t, "as_item") || !Reflect.has(t, "_internal"))
    throw new Error("`as_item` and `_internal` is required");
  const s = D(), o = ne({
    slot: void 0,
    index: t._internal.index,
    subIndex: t._internal.subIndex
  });
  s && s.subscribe((u) => {
    o.slotKey.set(u);
  }), te();
  const n = V($), i = ((d = g(n)) == null ? void 0 : d.as_item) || t.as_item, c = n ? i ? g(n)[i] : g(n) : {}, f = (u, m) => u ? J({
    ...u,
    ...m || {}
  }, e) : void 0, a = _({
    ...t,
    ...c,
    restProps: f(t.restProps, c),
    originalRestProps: t.restProps
  });
  return n ? (n.subscribe((u) => {
    const {
      as_item: m
    } = g(a);
    m && (u = u[m]), a.update((b) => ({
      ...b,
      ...u,
      restProps: f(b.restProps, u)
    }));
  }), [a, (u) => {
    const m = u.as_item ? g(n)[u.as_item] : g(n);
    return a.set({
      ...u,
      ...m,
      restProps: f(u.restProps, m),
      originalRestProps: u.restProps
    });
  }]) : [a, (u) => {
    a.set({
      ...u,
      restProps: f(u.restProps),
      originalRestProps: u.restProps
    });
  }];
}
const v = "$$ms-gr-slot-key";
function te() {
  w(v, _(void 0));
}
function D() {
  return V(v);
}
const se = "$$ms-gr-component-slot-context-key";
function ne({
  slot: t,
  index: e,
  subIndex: r
}) {
  return w(se, {
    slotKey: _(t),
    slotIndex: _(e),
    subSlotIndex: _(r)
  });
}
function I(t) {
  try {
    return typeof t == "string" ? new Function(`return (...args) => (${t})(...args)`)() : void 0;
  } catch {
    return;
  }
}
function re(t) {
  return t && t.__esModule && Object.prototype.hasOwnProperty.call(t, "default") ? t.default : t;
}
var B = {
  exports: {}
};
/*!
	Copyright (c) 2018 Jed Watson.
	Licensed under the MIT License (MIT), see
	http://jedwatson.github.io/classnames
*/
(function(t) {
  (function() {
    var e = {}.hasOwnProperty;
    function r() {
      for (var n = "", i = 0; i < arguments.length; i++) {
        var c = arguments[i];
        c && (n = o(n, s(c)));
      }
      return n;
    }
    function s(n) {
      if (typeof n == "string" || typeof n == "number")
        return n;
      if (typeof n != "object")
        return "";
      if (Array.isArray(n))
        return r.apply(null, n);
      if (n.toString !== Object.prototype.toString && !n.toString.toString().includes("[native code]"))
        return n.toString();
      var i = "";
      for (var c in n)
        e.call(n, c) && n[c] && (i = o(i, c));
      return i;
    }
    function o(n, i) {
      return i ? n ? n + " " + i : n + i : n;
    }
    t.exports ? (r.default = r, t.exports = r) : window.classNames = r;
  })();
})(B);
var oe = B.exports;
const ie = /* @__PURE__ */ re(oe), {
  getContext: le,
  setContext: ce
} = window.__gradio__svelte__internal;
function ue(t) {
  const e = `$$ms-gr-${t}-context-key`;
  function r(o = ["default"]) {
    const n = o.reduce((i, c) => (i[c] = _([]), i), {});
    return ce(e, {
      itemsMap: n,
      allowedSlots: o
    }), n;
  }
  function s() {
    const {
      itemsMap: o,
      allowedSlots: n
    } = le(e);
    return function(i, c, f) {
      o && (i ? o[i].update((a) => {
        const d = [...a];
        return n.includes(i) ? d[c] = f : d[c] = void 0, d;
      }) : n.includes("default") && o.default.update((a) => {
        const d = [...a];
        return d[c] = f, d;
      }));
    };
  }
  return {
    getItems: r,
    getSetItemFn: s
  };
}
const {
  getItems: Ee,
  getSetItemFn: ae
} = ue("table-expandable"), {
  SvelteComponent: fe,
  assign: M,
  check_outros: de,
  component_subscribe: E,
  compute_rest_props: T,
  create_slot: me,
  detach: _e,
  empty: z,
  exclude_internal_props: pe,
  flush: p,
  get_all_dirty_from_scope: be,
  get_slot_changes: ge,
  group_outros: xe,
  init: ye,
  insert_hydration: Pe,
  safe_not_equal: he,
  transition_in: k,
  transition_out: F,
  update_slot_base: Se
} = window.__gradio__svelte__internal;
function A(t) {
  let e;
  const r = (
    /*#slots*/
    t[17].default
  ), s = me(
    r,
    t,
    /*$$scope*/
    t[16],
    null
  );
  return {
    c() {
      s && s.c();
    },
    l(o) {
      s && s.l(o);
    },
    m(o, n) {
      s && s.m(o, n), e = !0;
    },
    p(o, n) {
      s && s.p && (!e || n & /*$$scope*/
      65536) && Se(
        s,
        r,
        o,
        /*$$scope*/
        o[16],
        e ? ge(
          r,
          /*$$scope*/
          o[16],
          n,
          null
        ) : be(
          /*$$scope*/
          o[16]
        ),
        null
      );
    },
    i(o) {
      e || (k(s, o), e = !0);
    },
    o(o) {
      F(s, o), e = !1;
    },
    d(o) {
      s && s.d(o);
    }
  };
}
function Re(t) {
  let e, r, s = (
    /*$mergedProps*/
    t[0].visible && A(t)
  );
  return {
    c() {
      s && s.c(), e = z();
    },
    l(o) {
      s && s.l(o), e = z();
    },
    m(o, n) {
      s && s.m(o, n), Pe(o, e, n), r = !0;
    },
    p(o, [n]) {
      /*$mergedProps*/
      o[0].visible ? s ? (s.p(o, n), n & /*$mergedProps*/
      1 && k(s, 1)) : (s = A(o), s.c(), k(s, 1), s.m(e.parentNode, e)) : s && (xe(), F(s, 1, 1, () => {
        s = null;
      }), de());
    },
    i(o) {
      r || (k(s), r = !0);
    },
    o(o) {
      F(s), r = !1;
    },
    d(o) {
      o && _e(e), s && s.d(o);
    }
  };
}
function Ce(t, e, r) {
  const s = ["gradio", "props", "_internal", "as_item", "visible", "elem_id", "elem_classes", "elem_style"];
  let o = T(e, s), n, i, c, f, {
    $$slots: a = {},
    $$scope: d
  } = e, {
    gradio: u
  } = e, {
    props: m = {}
  } = e;
  const b = _(m);
  E(t, b, (l) => r(15, f = l));
  let {
    _internal: y = {}
  } = e, {
    as_item: P
  } = e, {
    visible: h = !0
  } = e, {
    elem_id: S = ""
  } = e, {
    elem_classes: R = []
  } = e, {
    elem_style: C = {}
  } = e;
  const N = D();
  E(t, N, (l) => r(14, c = l));
  const [j, G] = ee({
    gradio: u,
    props: f,
    _internal: y,
    visible: h,
    elem_id: S,
    elem_classes: R,
    elem_style: C,
    as_item: P,
    restProps: o
  });
  E(t, j, (l) => r(0, i = l));
  const q = X();
  E(t, q, (l) => r(13, n = l));
  const O = Z(), H = ae();
  return t.$$set = (l) => {
    e = M(M({}, e), pe(l)), r(21, o = T(e, s)), "gradio" in l && r(5, u = l.gradio), "props" in l && r(6, m = l.props), "_internal" in l && r(7, y = l._internal), "as_item" in l && r(8, P = l.as_item), "visible" in l && r(9, h = l.visible), "elem_id" in l && r(10, S = l.elem_id), "elem_classes" in l && r(11, R = l.elem_classes), "elem_style" in l && r(12, C = l.elem_style), "$$scope" in l && r(16, d = l.$$scope);
  }, t.$$.update = () => {
    if (t.$$.dirty & /*props*/
    64 && b.update((l) => ({
      ...l,
      ...m
    })), G({
      gradio: u,
      props: f,
      _internal: y,
      visible: h,
      elem_id: S,
      elem_classes: R,
      elem_style: C,
      as_item: P,
      restProps: o
    }), t.$$.dirty & /*$mergedProps, $slotKey, $slots*/
    24577) {
      const l = L(i);
      H(c, i._internal.index || 0, {
        props: {
          style: i.elem_style,
          className: ie(i.elem_classes, "ms-gr-antd-table-expandable"),
          id: i.elem_id,
          ...i.restProps,
          ...i.props,
          ...l,
          expandedRowClassName: I(i.props.expandedRowClassName || i.restProps.expandedRowClassName),
          expandedRowRender: I(i.props.expandedRowRender || i.restProps.expandedRowRender),
          rowExpandable: I(i.props.rowExpandable || i.restProps.rowExpandable),
          expandIcon: I(i.props.expandIcon || i.restProps.expandIcon),
          columnTitle: i.props.columnTitle || i.restProps.columnTitle
        },
        slots: {
          ...n,
          expandIcon: {
            el: n.expandIcon,
            callback: O,
            clone: !0
          },
          expandedRowRender: {
            el: n.expandedRowRender,
            callback: O,
            clone: !0
          }
        }
      });
    }
  }, [i, b, N, j, q, u, m, y, P, h, S, R, C, n, c, f, d, a];
}
class Ke extends fe {
  constructor(e) {
    super(), ye(this, e, Ce, Re, he, {
      gradio: 5,
      props: 6,
      _internal: 7,
      as_item: 8,
      visible: 9,
      elem_id: 10,
      elem_classes: 11,
      elem_style: 12
    });
  }
  get gradio() {
    return this.$$.ctx[5];
  }
  set gradio(e) {
    this.$$set({
      gradio: e
    }), p();
  }
  get props() {
    return this.$$.ctx[6];
  }
  set props(e) {
    this.$$set({
      props: e
    }), p();
  }
  get _internal() {
    return this.$$.ctx[7];
  }
  set _internal(e) {
    this.$$set({
      _internal: e
    }), p();
  }
  get as_item() {
    return this.$$.ctx[8];
  }
  set as_item(e) {
    this.$$set({
      as_item: e
    }), p();
  }
  get visible() {
    return this.$$.ctx[9];
  }
  set visible(e) {
    this.$$set({
      visible: e
    }), p();
  }
  get elem_id() {
    return this.$$.ctx[10];
  }
  set elem_id(e) {
    this.$$set({
      elem_id: e
    }), p();
  }
  get elem_classes() {
    return this.$$.ctx[11];
  }
  set elem_classes(e) {
    this.$$set({
      elem_classes: e
    }), p();
  }
  get elem_style() {
    return this.$$.ctx[12];
  }
  set elem_style(e) {
    this.$$set({
      elem_style: e
    }), p();
  }
}
export {
  Ke as default
};
