import { g as ne, b as se } from "./Index-BbnpfSjt.js";
const y = window.ms_globals.React, re = window.ms_globals.React.forwardRef, oe = window.ms_globals.React.useRef, le = window.ms_globals.React.useState, ie = window.ms_globals.React.useEffect, ce = window.ms_globals.ReactDOM.createPortal;
function O() {
}
function ue(t, e) {
  return t != t ? e == e : t !== e || t && typeof t == "object" || typeof t == "function";
}
function ae(t, ...e) {
  if (t == null) {
    for (const n of e)
      n(void 0);
    return O;
  }
  const s = t.subscribe(...e);
  return s.unsubscribe ? () => s.unsubscribe() : s;
}
function x(t) {
  let e;
  return ae(t, (s) => e = s)(), e;
}
const C = [];
function g(t, e = O) {
  let s;
  const n = /* @__PURE__ */ new Set();
  function o(i) {
    if (ue(t, i) && (t = i, s)) {
      const c = !C.length;
      for (const u of n)
        u[1](), C.push(u, t);
      if (c) {
        for (let u = 0; u < C.length; u += 2)
          C[u][0](C[u + 1]);
        C.length = 0;
      }
    }
  }
  function r(i) {
    o(i(t));
  }
  function l(i, c = O) {
    const u = [i, c];
    return n.add(u), n.size === 1 && (s = e(o, r) || O), i(t), () => {
      n.delete(u), n.size === 0 && s && (s(), s = null);
    };
  }
  return {
    set: o,
    update: r,
    subscribe: l
  };
}
const {
  getContext: V,
  setContext: v
} = window.__gradio__svelte__internal, fe = "$$ms-gr-slots-key";
function de() {
  const t = g({});
  return v(fe, t);
}
const me = "$$ms-gr-render-slot-context-key";
function _e() {
  const t = v(me, g({}));
  return (e, s) => {
    t.update((n) => typeof s == "function" ? {
      ...n,
      [e]: s(n[e])
    } : {
      ...n,
      [e]: s
    });
  };
}
const pe = "$$ms-gr-context-key";
function ge(t, e, s) {
  var m;
  if (!Reflect.has(t, "as_item") || !Reflect.has(t, "_internal"))
    throw new Error("`as_item` and `_internal` is required");
  const n = J(), o = ye({
    slot: void 0,
    index: t._internal.index,
    subIndex: t._internal.subIndex
  });
  n && n.subscribe((d) => {
    o.slotKey.set(d);
  }), he();
  const r = V(pe), l = ((m = x(r)) == null ? void 0 : m.as_item) || t.as_item, i = r ? l ? x(r)[l] : x(r) : {}, c = (d, a) => d ? ne({
    ...d,
    ...a || {}
  }, e) : void 0, u = g({
    ...t,
    ...i,
    restProps: c(t.restProps, i),
    originalRestProps: t.restProps
  });
  return r ? (r.subscribe((d) => {
    const {
      as_item: a
    } = x(u);
    a && (d = d[a]), u.update((_) => ({
      ..._,
      ...d,
      restProps: c(_.restProps, d)
    }));
  }), [u, (d) => {
    const a = d.as_item ? x(r)[d.as_item] : x(r);
    return u.set({
      ...d,
      ...a,
      restProps: c(d.restProps, a),
      originalRestProps: d.restProps
    });
  }]) : [u, (d) => {
    u.set({
      ...d,
      restProps: c(d.restProps),
      originalRestProps: d.restProps
    });
  }];
}
const B = "$$ms-gr-slot-key";
function he() {
  v(B, g(void 0));
}
function J() {
  return V(B);
}
const be = "$$ms-gr-component-slot-context-key";
function ye({
  slot: t,
  index: e,
  subIndex: s
}) {
  return v(be, {
    slotKey: g(t),
    slotIndex: g(e),
    subSlotIndex: g(s)
  });
}
function F(t) {
  try {
    return typeof t == "string" ? new Function(`return (...args) => (${t})(...args)`)() : void 0;
  } catch {
    return;
  }
}
function xe(t) {
  return t && t.__esModule && Object.prototype.hasOwnProperty.call(t, "default") ? t.default : t;
}
var Y = {
  exports: {}
}, j = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Ce = y, Pe = Symbol.for("react.element"), Se = Symbol.for("react.fragment"), Ee = Object.prototype.hasOwnProperty, we = Ce.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Re = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function Q(t, e, s) {
  var n, o = {}, r = null, l = null;
  s !== void 0 && (r = "" + s), e.key !== void 0 && (r = "" + e.key), e.ref !== void 0 && (l = e.ref);
  for (n in e) Ee.call(e, n) && !Re.hasOwnProperty(n) && (o[n] = e[n]);
  if (t && t.defaultProps) for (n in e = t.defaultProps, e) o[n] === void 0 && (o[n] = e[n]);
  return {
    $$typeof: Pe,
    type: t,
    key: r,
    ref: l,
    props: o,
    _owner: we.current
  };
}
j.Fragment = Se;
j.jsx = Q;
j.jsxs = Q;
Y.exports = j;
var z = Y.exports;
const Ie = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Oe(t) {
  return t ? Object.keys(t).reduce((e, s) => {
    const n = t[s];
    return typeof n == "number" && !Ie.includes(s) ? e[s] = n + "px" : e[s] = n, e;
  }, {}) : {};
}
function N(t) {
  const e = [], s = t.cloneNode(!1);
  if (t._reactElement)
    return e.push(ce(y.cloneElement(t._reactElement, {
      ...t._reactElement.props,
      children: y.Children.toArray(t._reactElement.props.children).map((o) => {
        if (y.isValidElement(o) && o.props.__slot__) {
          const {
            portals: r,
            clonedElement: l
          } = N(o.props.el);
          return y.cloneElement(o, {
            ...o.props,
            el: l,
            children: [...y.Children.toArray(o.props.children), ...r]
          });
        }
        return null;
      })
    }), s)), {
      clonedElement: s,
      portals: e
    };
  Object.keys(t.getEventListeners()).forEach((o) => {
    t.getEventListeners(o).forEach(({
      listener: l,
      type: i,
      useCapture: c
    }) => {
      s.addEventListener(i, l, c);
    });
  });
  const n = Array.from(t.childNodes);
  for (let o = 0; o < n.length; o++) {
    const r = n[o];
    if (r.nodeType === 1) {
      const {
        clonedElement: l,
        portals: i
      } = N(r);
      e.push(...i), s.appendChild(l);
    } else r.nodeType === 3 && s.appendChild(r.cloneNode());
  }
  return {
    clonedElement: s,
    portals: e
  };
}
function ke(t, e) {
  t && (typeof t == "function" ? t(e) : t.current = e);
}
const D = re(({
  slot: t,
  clone: e,
  className: s,
  style: n
}, o) => {
  const r = oe(), [l, i] = le([]);
  return ie(() => {
    var d;
    if (!r.current || !t)
      return;
    let c = t;
    function u() {
      let a = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (a = c.children[0], a.tagName.toLowerCase() === "react-portal-target" && a.children[0] && (a = a.children[0])), ke(o, a), s && a.classList.add(...s.split(" ")), n) {
        const _ = Oe(n);
        Object.keys(_).forEach((p) => {
          a.style[p] = _[p];
        });
      }
    }
    let m = null;
    if (e && window.MutationObserver) {
      let a = function() {
        var b;
        const {
          portals: _,
          clonedElement: p
        } = N(t);
        c = p, i(_), c.style.display = "contents", u(), (b = r.current) == null || b.appendChild(c);
      };
      a(), m = new window.MutationObserver(() => {
        var _, p;
        (_ = r.current) != null && _.contains(c) && ((p = r.current) == null || p.removeChild(c)), a();
      }), m.observe(t, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", u(), (d = r.current) == null || d.appendChild(c);
    return () => {
      var a, _;
      c.style.display = "", (a = r.current) != null && a.contains(c) && ((_ = r.current) == null || _.removeChild(c)), m == null || m.disconnect();
    };
  }, [t, e, s, n, o]), y.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
});
function X(t, e) {
  return t.filter(Boolean).map((s) => {
    if (typeof s != "object")
      return s;
    const n = {
      ...s.props
    };
    let o = n;
    Object.keys(s.slots).forEach((l) => {
      if (!s.slots[l] || !(s.slots[l] instanceof Element) && !s.slots[l].el)
        return;
      const i = l.split(".");
      i.forEach((a, _) => {
        o[a] || (o[a] = {}), _ !== i.length - 1 && (o = n[a]);
      });
      const c = s.slots[l];
      let u, m, d = !1;
      c instanceof Element ? u = c : (u = c.el, m = c.callback, d = c.clone || !1), o[i[i.length - 1]] = u ? m ? (...a) => (m(i[i.length - 1], a), /* @__PURE__ */ z.jsx(D, {
        slot: u,
        clone: d || (e == null ? void 0 : e.clone)
      })) : /* @__PURE__ */ z.jsx(D, {
        slot: u,
        clone: d || (e == null ? void 0 : e.clone)
      }) : o[i[i.length - 1]], o = n;
    });
    const r = "children";
    return s[r] && (n[r] = X(s[r], e)), n;
  });
}
var Z = {
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
    function s() {
      for (var r = "", l = 0; l < arguments.length; l++) {
        var i = arguments[l];
        i && (r = o(r, n(i)));
      }
      return r;
    }
    function n(r) {
      if (typeof r == "string" || typeof r == "number")
        return r;
      if (typeof r != "object")
        return "";
      if (Array.isArray(r))
        return s.apply(null, r);
      if (r.toString !== Object.prototype.toString && !r.toString.toString().includes("[native code]"))
        return r.toString();
      var l = "";
      for (var i in r)
        e.call(r, i) && r[i] && (l = o(l, i));
      return l;
    }
    function o(r, l) {
      return l ? r ? r + " " + l : r + l : r;
    }
    t.exports ? (s.default = s, t.exports = s) : window.classNames = s;
  })();
})(Z);
var ve = Z.exports;
const je = /* @__PURE__ */ xe(ve), {
  getContext: Fe,
  setContext: Ne
} = window.__gradio__svelte__internal;
function $(t) {
  const e = `$$ms-gr-${t}-context-key`;
  function s(o = ["default"]) {
    const r = o.reduce((l, i) => (l[i] = g([]), l), {});
    return Ne(e, {
      itemsMap: r,
      allowedSlots: o
    }), r;
  }
  function n() {
    const {
      itemsMap: o,
      allowedSlots: r
    } = Fe(e);
    return function(l, i, c) {
      o && (l ? o[l].update((u) => {
        const m = [...u];
        return r.includes(l) ? m[i] = c : m[i] = void 0, m;
      }) : r.includes("default") && o.default.update((u) => {
        const m = [...u];
        return m[i] = c, m;
      }));
    };
  }
  return {
    getItems: s,
    getSetItemFn: n
  };
}
const {
  getItems: Te,
  getSetItemFn: Xe
} = $("table-row-selection-selection"), {
  getItems: Ze,
  getSetItemFn: Le
} = $("table-row-selection"), {
  SvelteComponent: Ae,
  assign: W,
  check_outros: Ke,
  component_subscribe: P,
  compute_rest_props: G,
  create_slot: qe,
  detach: Me,
  empty: H,
  exclude_internal_props: ze,
  flush: h,
  get_all_dirty_from_scope: De,
  get_slot_changes: We,
  group_outros: Ge,
  init: He,
  insert_hydration: Ue,
  safe_not_equal: Ve,
  transition_in: k,
  transition_out: T,
  update_slot_base: Be
} = window.__gradio__svelte__internal;
function U(t) {
  let e;
  const s = (
    /*#slots*/
    t[19].default
  ), n = qe(
    s,
    t,
    /*$$scope*/
    t[18],
    null
  );
  return {
    c() {
      n && n.c();
    },
    l(o) {
      n && n.l(o);
    },
    m(o, r) {
      n && n.m(o, r), e = !0;
    },
    p(o, r) {
      n && n.p && (!e || r & /*$$scope*/
      262144) && Be(
        n,
        s,
        o,
        /*$$scope*/
        o[18],
        e ? We(
          s,
          /*$$scope*/
          o[18],
          r,
          null
        ) : De(
          /*$$scope*/
          o[18]
        ),
        null
      );
    },
    i(o) {
      e || (k(n, o), e = !0);
    },
    o(o) {
      T(n, o), e = !1;
    },
    d(o) {
      n && n.d(o);
    }
  };
}
function Je(t) {
  let e, s, n = (
    /*$mergedProps*/
    t[0].visible && U(t)
  );
  return {
    c() {
      n && n.c(), e = H();
    },
    l(o) {
      n && n.l(o), e = H();
    },
    m(o, r) {
      n && n.m(o, r), Ue(o, e, r), s = !0;
    },
    p(o, [r]) {
      /*$mergedProps*/
      o[0].visible ? n ? (n.p(o, r), r & /*$mergedProps*/
      1 && k(n, 1)) : (n = U(o), n.c(), k(n, 1), n.m(e.parentNode, e)) : n && (Ge(), T(n, 1, 1, () => {
        n = null;
      }), Ke());
    },
    i(o) {
      s || (k(n), s = !0);
    },
    o(o) {
      T(n), s = !1;
    },
    d(o) {
      o && Me(e), n && n.d(o);
    }
  };
}
function Ye(t, e, s) {
  const n = ["gradio", "props", "_internal", "as_item", "visible", "elem_id", "elem_classes", "elem_style"];
  let o = G(e, n), r, l, i, c, u, {
    $$slots: m = {},
    $$scope: d
  } = e, {
    gradio: a
  } = e, {
    props: _ = {}
  } = e;
  const p = g(_);
  P(t, p, (f) => s(17, u = f));
  let {
    _internal: b = {}
  } = e, {
    as_item: S
  } = e, {
    visible: E = !0
  } = e, {
    elem_id: w = ""
  } = e, {
    elem_classes: R = []
  } = e, {
    elem_style: I = {}
  } = e;
  const L = J();
  P(t, L, (f) => s(16, c = f));
  const [A, ee] = ge({
    gradio: a,
    props: u,
    _internal: b,
    visible: E,
    elem_id: w,
    elem_classes: R,
    elem_style: I,
    as_item: S,
    restProps: o
  });
  P(t, A, (f) => s(0, l = f));
  const K = _e(), q = de();
  P(t, q, (f) => s(14, r = f));
  const {
    selections: M
  } = Te(["selections"]);
  P(t, M, (f) => s(15, i = f));
  const te = Le();
  return t.$$set = (f) => {
    e = W(W({}, e), ze(f)), s(23, o = G(e, n)), "gradio" in f && s(6, a = f.gradio), "props" in f && s(7, _ = f.props), "_internal" in f && s(8, b = f._internal), "as_item" in f && s(9, S = f.as_item), "visible" in f && s(10, E = f.visible), "elem_id" in f && s(11, w = f.elem_id), "elem_classes" in f && s(12, R = f.elem_classes), "elem_style" in f && s(13, I = f.elem_style), "$$scope" in f && s(18, d = f.$$scope);
  }, t.$$.update = () => {
    if (t.$$.dirty & /*props*/
    128 && p.update((f) => ({
      ...f,
      ..._
    })), ee({
      gradio: a,
      props: u,
      _internal: b,
      visible: E,
      elem_id: w,
      elem_classes: R,
      elem_style: I,
      as_item: S,
      restProps: o
    }), t.$$.dirty & /*$mergedProps, $slotKey, $selectionsItems, $slots*/
    114689) {
      const f = se(l);
      te(c, l._internal.index || 0, {
        props: {
          style: l.elem_style,
          className: je(l.elem_classes, "ms-gr-antd-table-row-selection"),
          id: l.elem_id,
          ...l.restProps,
          ...l.props,
          ...f,
          selections: l.props.selections || l.restProps.selections || X(i),
          onCell: F(l.props.onCell || l.restProps.onCell),
          getCheckboxProps: F(l.props.getCheckboxProps || l.restProps.getCheckboxProps),
          renderCell: F(l.props.renderCell || l.restProps.renderCell),
          columnTitle: l.props.columnTitle || l.restProps.columnTitle
        },
        slots: {
          ...r,
          columnTitle: {
            el: r.columnTitle,
            callback: K,
            clone: !0
          },
          renderCell: {
            el: r.renderCell,
            callback: K,
            clone: !0
          }
        }
      });
    }
  }, [l, p, L, A, q, M, a, _, b, S, E, w, R, I, r, i, c, u, d, m];
}
class $e extends Ae {
  constructor(e) {
    super(), He(this, e, Ye, Je, Ve, {
      gradio: 6,
      props: 7,
      _internal: 8,
      as_item: 9,
      visible: 10,
      elem_id: 11,
      elem_classes: 12,
      elem_style: 13
    });
  }
  get gradio() {
    return this.$$.ctx[6];
  }
  set gradio(e) {
    this.$$set({
      gradio: e
    }), h();
  }
  get props() {
    return this.$$.ctx[7];
  }
  set props(e) {
    this.$$set({
      props: e
    }), h();
  }
  get _internal() {
    return this.$$.ctx[8];
  }
  set _internal(e) {
    this.$$set({
      _internal: e
    }), h();
  }
  get as_item() {
    return this.$$.ctx[9];
  }
  set as_item(e) {
    this.$$set({
      as_item: e
    }), h();
  }
  get visible() {
    return this.$$.ctx[10];
  }
  set visible(e) {
    this.$$set({
      visible: e
    }), h();
  }
  get elem_id() {
    return this.$$.ctx[11];
  }
  set elem_id(e) {
    this.$$set({
      elem_id: e
    }), h();
  }
  get elem_classes() {
    return this.$$.ctx[12];
  }
  set elem_classes(e) {
    this.$$set({
      elem_classes: e
    }), h();
  }
  get elem_style() {
    return this.$$.ctx[13];
  }
  set elem_style(e) {
    this.$$set({
      elem_style: e
    }), h();
  }
}
export {
  $e as default
};
