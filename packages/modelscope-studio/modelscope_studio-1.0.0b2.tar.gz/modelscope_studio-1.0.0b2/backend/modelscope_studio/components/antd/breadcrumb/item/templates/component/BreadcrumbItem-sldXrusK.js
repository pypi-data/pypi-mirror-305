import { g as Oe, b as je } from "./Index-BBJUr1YQ.js";
const b = window.ms_globals.React, ke = window.ms_globals.React.forwardRef, Ne = window.ms_globals.React.useRef, Fe = window.ms_globals.React.useState, Le = window.ms_globals.React.useEffect, Me = window.ms_globals.ReactDOM.createPortal;
function j() {
}
function Ae(t, e) {
  return t != t ? e == e : t !== e || t && typeof t == "object" || typeof t == "function";
}
function Ke(t, ...e) {
  if (t == null) {
    for (const n of e)
      n(void 0);
    return j;
  }
  const o = t.subscribe(...e);
  return o.unsubscribe ? () => o.unsubscribe() : o;
}
function y(t) {
  let e;
  return Ke(t, (o) => e = o)(), e;
}
const w = [];
function g(t, e = j) {
  let o;
  const n = /* @__PURE__ */ new Set();
  function s(i) {
    if (Ae(t, i) && (t = i, o)) {
      const c = !w.length;
      for (const u of n)
        u[1](), w.push(u, t);
      if (c) {
        for (let u = 0; u < w.length; u += 2)
          w[u][0](w[u + 1]);
        w.length = 0;
      }
    }
  }
  function r(i) {
    s(i(t));
  }
  function l(i, c = j) {
    const u = [i, c];
    return n.add(u), n.size === 1 && (o = e(s, r) || j), i(t), () => {
      n.delete(u), n.size === 0 && o && (o(), o = null);
    };
  }
  return {
    set: s,
    update: r,
    subscribe: l
  };
}
const {
  getContext: ye,
  setContext: N
} = window.__gradio__svelte__internal, qe = "$$ms-gr-slots-key";
function Be() {
  const t = g({});
  return N(qe, t);
}
const Te = "$$ms-gr-render-slot-context-key";
function ze() {
  const t = N(Te, g({}));
  return (e, o) => {
    t.update((n) => typeof o == "function" ? {
      ...n,
      [e]: o(n[e])
    } : {
      ...n,
      [e]: o
    });
  };
}
const De = "$$ms-gr-context-key";
function We(t, e, o) {
  var m;
  if (!Reflect.has(t, "as_item") || !Reflect.has(t, "_internal"))
    throw new Error("`as_item` and `_internal` is required");
  const n = xe(), s = Ue({
    slot: void 0,
    index: t._internal.index,
    subIndex: t._internal.subIndex
  });
  n && n.subscribe((f) => {
    s.slotKey.set(f);
  }), Ge();
  const r = ye(De), l = ((m = y(r)) == null ? void 0 : m.as_item) || t.as_item, i = r ? l ? y(r)[l] : y(r) : {}, c = (f, a) => f ? Oe({
    ...f,
    ...a || {}
  }, e) : void 0, u = g({
    ...t,
    ...i,
    restProps: c(t.restProps, i),
    originalRestProps: t.restProps
  });
  return r ? (r.subscribe((f) => {
    const {
      as_item: a
    } = y(u);
    a && (f = f[a]), u.update((p) => ({
      ...p,
      ...f,
      restProps: c(p.restProps, f)
    }));
  }), [u, (f) => {
    const a = f.as_item ? y(r)[f.as_item] : y(r);
    return u.set({
      ...f,
      ...a,
      restProps: c(f.restProps, a),
      originalRestProps: f.restProps
    });
  }]) : [u, (f) => {
    u.set({
      ...f,
      restProps: c(f.restProps),
      originalRestProps: f.restProps
    });
  }];
}
const we = "$$ms-gr-slot-key";
function Ge() {
  N(we, g(void 0));
}
function xe() {
  return ye(we);
}
const He = "$$ms-gr-component-slot-context-key";
function Ue({
  slot: t,
  index: e,
  subIndex: o
}) {
  return N(He, {
    slotKey: g(t),
    slotIndex: g(e),
    subSlotIndex: g(o)
  });
}
function Ve(t) {
  try {
    return typeof t == "string" ? new Function(`return (...args) => (${t})(...args)`)() : void 0;
  } catch {
    return;
  }
}
function Je(t) {
  return t && t.__esModule && Object.prototype.hasOwnProperty.call(t, "default") ? t.default : t;
}
var Ie = {
  exports: {}
}, F = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Ye = b, Qe = Symbol.for("react.element"), Xe = Symbol.for("react.fragment"), Ze = Object.prototype.hasOwnProperty, $e = Ye.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, et = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function Ee(t, e, o) {
  var n, s = {}, r = null, l = null;
  o !== void 0 && (r = "" + o), e.key !== void 0 && (r = "" + e.key), e.ref !== void 0 && (l = e.ref);
  for (n in e) Ze.call(e, n) && !et.hasOwnProperty(n) && (s[n] = e[n]);
  if (t && t.defaultProps) for (n in e = t.defaultProps, e) s[n] === void 0 && (s[n] = e[n]);
  return {
    $$typeof: Qe,
    type: t,
    key: r,
    ref: l,
    props: s,
    _owner: $e.current
  };
}
F.Fragment = Xe;
F.jsx = Ee;
F.jsxs = Ee;
Ie.exports = F;
var A = Ie.exports;
const tt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function nt(t) {
  return t ? Object.keys(t).reduce((e, o) => {
    const n = t[o];
    return typeof n == "number" && !tt.includes(o) ? e[o] = n + "px" : e[o] = n, e;
  }, {}) : {};
}
function K(t) {
  const e = [], o = t.cloneNode(!1);
  if (t._reactElement)
    return e.push(Me(b.cloneElement(t._reactElement, {
      ...t._reactElement.props,
      children: b.Children.toArray(t._reactElement.props.children).map((s) => {
        if (b.isValidElement(s) && s.props.__slot__) {
          const {
            portals: r,
            clonedElement: l
          } = K(s.props.el);
          return b.cloneElement(s, {
            ...s.props,
            el: l,
            children: [...b.Children.toArray(s.props.children), ...r]
          });
        }
        return null;
      })
    }), o)), {
      clonedElement: o,
      portals: e
    };
  Object.keys(t.getEventListeners()).forEach((s) => {
    t.getEventListeners(s).forEach(({
      listener: l,
      type: i,
      useCapture: c
    }) => {
      o.addEventListener(i, l, c);
    });
  });
  const n = Array.from(t.childNodes);
  for (let s = 0; s < n.length; s++) {
    const r = n[s];
    if (r.nodeType === 1) {
      const {
        clonedElement: l,
        portals: i
      } = K(r);
      e.push(...i), o.appendChild(l);
    } else r.nodeType === 3 && o.appendChild(r.cloneNode());
  }
  return {
    clonedElement: o,
    portals: e
  };
}
function rt(t, e) {
  t && (typeof t == "function" ? t(e) : t.current = e);
}
const q = ke(({
  slot: t,
  clone: e,
  className: o,
  style: n
}, s) => {
  const r = Ne(), [l, i] = Fe([]);
  return Le(() => {
    var f;
    if (!r.current || !t)
      return;
    let c = t;
    function u() {
      let a = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (a = c.children[0], a.tagName.toLowerCase() === "react-portal-target" && a.children[0] && (a = a.children[0])), rt(s, a), o && a.classList.add(...o.split(" ")), n) {
        const p = nt(n);
        Object.keys(p).forEach((_) => {
          a.style[_] = p[_];
        });
      }
    }
    let m = null;
    if (e && window.MutationObserver) {
      let a = function() {
        var P;
        const {
          portals: p,
          clonedElement: _
        } = K(t);
        c = _, i(p), c.style.display = "contents", u(), (P = r.current) == null || P.appendChild(c);
      };
      a(), m = new window.MutationObserver(() => {
        var p, _;
        (p = r.current) != null && p.contains(c) && ((_ = r.current) == null || _.removeChild(c)), a();
      }), m.observe(t, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", u(), (f = r.current) == null || f.appendChild(c);
    return () => {
      var a, p;
      c.style.display = "", (a = r.current) != null && a.contains(c) && ((p = r.current) == null || p.removeChild(c)), m == null || m.disconnect();
    };
  }, [t, e, o, n, s]), b.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
});
function B(t, e) {
  return t.filter(Boolean).map((o) => {
    if (typeof o != "object")
      return o;
    const n = {
      ...o.props
    };
    let s = n;
    Object.keys(o.slots).forEach((l) => {
      if (!o.slots[l] || !(o.slots[l] instanceof Element) && !o.slots[l].el)
        return;
      const i = l.split(".");
      i.forEach((a, p) => {
        s[a] || (s[a] = {}), p !== i.length - 1 && (s = n[a]);
      });
      const c = o.slots[l];
      let u, m, f = !1;
      c instanceof Element ? u = c : (u = c.el, m = c.callback, f = c.clone || !1), s[i[i.length - 1]] = u ? m ? (...a) => (m(i[i.length - 1], a), /* @__PURE__ */ A.jsx(q, {
        slot: u,
        clone: f || (e == null ? void 0 : e.clone)
      })) : /* @__PURE__ */ A.jsx(q, {
        slot: u,
        clone: f || (e == null ? void 0 : e.clone)
      }) : s[i[i.length - 1]], s = n;
    });
    const r = "children";
    return o[r] && (n[r] = B(o[r], e)), n;
  });
}
function T(t, e) {
  return t ? /* @__PURE__ */ A.jsx(q, {
    slot: t,
    clone: e == null ? void 0 : e.clone
  }) : null;
}
function M({
  key: t,
  setSlotParams: e,
  slots: o
}, n) {
  return (...s) => (e(t, s), T(o[t], {
    clone: !0,
    ...n
  }));
}
var Se = {
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
    function o() {
      for (var r = "", l = 0; l < arguments.length; l++) {
        var i = arguments[l];
        i && (r = s(r, n(i)));
      }
      return r;
    }
    function n(r) {
      if (typeof r == "string" || typeof r == "number")
        return r;
      if (typeof r != "object")
        return "";
      if (Array.isArray(r))
        return o.apply(null, r);
      if (r.toString !== Object.prototype.toString && !r.toString.toString().includes("[native code]"))
        return r.toString();
      var l = "";
      for (var i in r)
        e.call(r, i) && r[i] && (l = s(l, i));
      return l;
    }
    function s(r, l) {
      return l ? r ? r + " " + l : r + l : r;
    }
    t.exports ? (o.default = o, t.exports = o) : window.classNames = o;
  })();
})(Se);
var ot = Se.exports;
const st = /* @__PURE__ */ Je(ot), {
  getContext: lt,
  setContext: it
} = window.__gradio__svelte__internal;
function Ce(t) {
  const e = `$$ms-gr-${t}-context-key`;
  function o(s = ["default"]) {
    const r = s.reduce((l, i) => (l[i] = g([]), l), {});
    return it(e, {
      itemsMap: r,
      allowedSlots: s
    }), r;
  }
  function n() {
    const {
      itemsMap: s,
      allowedSlots: r
    } = lt(e);
    return function(l, i, c) {
      s && (l ? s[l].update((u) => {
        const m = [...u];
        return r.includes(l) ? m[i] = c : m[i] = void 0, m;
      }) : r.includes("default") && s.default.update((u) => {
        const m = [...u];
        return m[i] = c, m;
      }));
    };
  }
  return {
    getItems: o,
    getSetItemFn: n
  };
}
const {
  getItems: ct,
  getSetItemFn: St
} = Ce("menu"), {
  getItems: Ct,
  getSetItemFn: ut
} = Ce("breadcrumb"), {
  SvelteComponent: dt,
  assign: ge,
  check_outros: at,
  component_subscribe: x,
  compute_rest_props: he,
  create_slot: ft,
  detach: mt,
  empty: be,
  exclude_internal_props: pt,
  flush: h,
  get_all_dirty_from_scope: _t,
  get_slot_changes: gt,
  group_outros: ht,
  init: bt,
  insert_hydration: Pt,
  safe_not_equal: yt,
  transition_in: k,
  transition_out: z,
  update_slot_base: wt
} = window.__gradio__svelte__internal;
function Pe(t) {
  let e;
  const o = (
    /*#slots*/
    t[21].default
  ), n = ft(
    o,
    t,
    /*$$scope*/
    t[20],
    null
  );
  return {
    c() {
      n && n.c();
    },
    l(s) {
      n && n.l(s);
    },
    m(s, r) {
      n && n.m(s, r), e = !0;
    },
    p(s, r) {
      n && n.p && (!e || r & /*$$scope*/
      1048576) && wt(
        n,
        o,
        s,
        /*$$scope*/
        s[20],
        e ? gt(
          o,
          /*$$scope*/
          s[20],
          r,
          null
        ) : _t(
          /*$$scope*/
          s[20]
        ),
        null
      );
    },
    i(s) {
      e || (k(n, s), e = !0);
    },
    o(s) {
      z(n, s), e = !1;
    },
    d(s) {
      n && n.d(s);
    }
  };
}
function xt(t) {
  let e, o, n = (
    /*$mergedProps*/
    t[0].visible && Pe(t)
  );
  return {
    c() {
      n && n.c(), e = be();
    },
    l(s) {
      n && n.l(s), e = be();
    },
    m(s, r) {
      n && n.m(s, r), Pt(s, e, r), o = !0;
    },
    p(s, [r]) {
      /*$mergedProps*/
      s[0].visible ? n ? (n.p(s, r), r & /*$mergedProps*/
      1 && k(n, 1)) : (n = Pe(s), n.c(), k(n, 1), n.m(e.parentNode, e)) : n && (ht(), z(n, 1, 1, () => {
        n = null;
      }), at());
    },
    i(s) {
      o || (k(n), o = !0);
    },
    o(s) {
      z(n), o = !1;
    },
    d(s) {
      s && mt(e), n && n.d(s);
    }
  };
}
function It(t, e, o) {
  const n = ["gradio", "props", "_internal", "as_item", "visible", "elem_id", "elem_classes", "elem_style"];
  let s = he(e, n), r, l, i, c, u, m, {
    $$slots: f = {},
    $$scope: a
  } = e, {
    gradio: p
  } = e, {
    props: _ = {}
  } = e;
  const P = g(_);
  x(t, P, (d) => o(19, m = d));
  let {
    _internal: I = {}
  } = e, {
    as_item: E
  } = e, {
    visible: S = !0
  } = e, {
    elem_id: C = ""
  } = e, {
    elem_classes: R = []
  } = e, {
    elem_style: v = {}
  } = e;
  const D = xe();
  x(t, D, (d) => o(16, i = d));
  const [W, Re] = We({
    gradio: p,
    props: m,
    _internal: I,
    visible: S,
    elem_id: C,
    elem_classes: R,
    elem_style: v,
    as_item: E,
    restProps: s
  });
  x(t, W, (d) => o(0, l = d));
  const G = Be();
  x(t, G, (d) => o(15, r = d));
  const ve = ut(), L = ze(), {
    "menu.items": H,
    "dropdownProps.menu.items": U
  } = ct(["menu.items", "dropdownProps.menu.items"]);
  return x(t, H, (d) => o(18, u = d)), x(t, U, (d) => o(17, c = d)), t.$$set = (d) => {
    e = ge(ge({}, e), pt(d)), o(25, s = he(e, n)), "gradio" in d && o(7, p = d.gradio), "props" in d && o(8, _ = d.props), "_internal" in d && o(9, I = d._internal), "as_item" in d && o(10, E = d.as_item), "visible" in d && o(11, S = d.visible), "elem_id" in d && o(12, C = d.elem_id), "elem_classes" in d && o(13, R = d.elem_classes), "elem_style" in d && o(14, v = d.elem_style), "$$scope" in d && o(20, a = d.$$scope);
  }, t.$$.update = () => {
    var d, V, J, Y, Q, X, Z, $, ee, te, ne, re, oe, se, le, ie, ce, ue, de, ae, fe, me;
    if (t.$$.dirty & /*props*/
    256 && P.update((O) => ({
      ...O,
      ..._
    })), Re({
      gradio: p,
      props: m,
      _internal: I,
      visible: S,
      elem_id: C,
      elem_classes: R,
      elem_style: v,
      as_item: E,
      restProps: s
    }), t.$$.dirty & /*$mergedProps, $menuItems, $slots, $dropdownMenuItems, $slotKey*/
    491521) {
      const O = {
        ...l.restProps.menu || {},
        ...l.props.menu || {},
        items: (d = l.props.menu) != null && d.items || (V = l.restProps.menu) != null && V.items || u.length > 0 ? B(u) : void 0,
        expandIcon: M({
          setSlotParams: L,
          slots: r,
          key: "menu.expandIcon"
        }, {
          clone: !0
        }) || ((J = l.props.menu) == null ? void 0 : J.expandIcon) || ((Y = l.restProps.menu) == null ? void 0 : Y.expandIcon),
        overflowedIndicator: T(r["menu.overflowedIndicator"]) || ((Q = l.props.menu) == null ? void 0 : Q.overflowedIndicator) || ((X = l.restProps.menu) == null ? void 0 : X.overflowedIndicator)
      }, pe = {
        ...((Z = l.restProps.dropdownProps) == null ? void 0 : Z.menu) || {},
        ...(($ = l.props.dropdownProps) == null ? void 0 : $.menu) || {},
        items: (te = (ee = l.props.dropdownProps) == null ? void 0 : ee.menu) != null && te.items || (re = (ne = l.restProps.dropdownProps) == null ? void 0 : ne.menu) != null && re.items || c.length > 0 ? B(c) : void 0,
        expandIcon: M({
          setSlotParams: L,
          slots: r,
          key: "dropdownProps.menu.expandIcon"
        }, {
          clone: !0
        }) || ((se = (oe = l.props.dropdownProps) == null ? void 0 : oe.menu) == null ? void 0 : se.expandIcon) || ((ie = (le = l.restProps.dropdownProps) == null ? void 0 : le.menu) == null ? void 0 : ie.expandIcon),
        overflowedIndicator: T(r["dropdownProps.menu.overflowedIndicator"]) || ((ue = (ce = l.props.dropdownProps) == null ? void 0 : ce.menu) == null ? void 0 : ue.overflowedIndicator) || ((ae = (de = l.restProps.dropdownProps) == null ? void 0 : de.menu) == null ? void 0 : ae.overflowedIndicator)
      }, _e = {
        ...l.restProps.dropdownProps || {},
        ...l.props.dropdownProps || {},
        dropdownRender: r["dropdownProps.dropdownRender"] ? M({
          setSlotParams: L,
          slots: r,
          key: "dropdownProps.dropdownRender"
        }, {
          clone: !0
        }) : Ve(((fe = l.props.dropdownProps) == null ? void 0 : fe.dropdownRender) || ((me = l.restProps.dropdownProps) == null ? void 0 : me.dropdownRender)),
        menu: Object.values(pe).filter(Boolean).length > 0 ? pe : void 0
      };
      ve(i, l._internal.index || 0, {
        props: {
          style: l.elem_style,
          className: st(l.elem_classes, "ms-gr-antd-breadcrumb-item"),
          id: l.elem_id,
          ...l.restProps,
          ...l.props,
          ...je(l),
          menu: Object.values(O).filter(Boolean).length > 0 ? O : void 0,
          dropdownProps: Object.values(_e).filter(Boolean).length > 0 ? _e : void 0
        },
        slots: {
          title: r.title
        }
      });
    }
  }, [l, P, D, W, G, H, U, p, _, I, E, S, C, R, v, r, i, c, u, m, a, f];
}
class Rt extends dt {
  constructor(e) {
    super(), bt(this, e, It, xt, yt, {
      gradio: 7,
      props: 8,
      _internal: 9,
      as_item: 10,
      visible: 11,
      elem_id: 12,
      elem_classes: 13,
      elem_style: 14
    });
  }
  get gradio() {
    return this.$$.ctx[7];
  }
  set gradio(e) {
    this.$$set({
      gradio: e
    }), h();
  }
  get props() {
    return this.$$.ctx[8];
  }
  set props(e) {
    this.$$set({
      props: e
    }), h();
  }
  get _internal() {
    return this.$$.ctx[9];
  }
  set _internal(e) {
    this.$$set({
      _internal: e
    }), h();
  }
  get as_item() {
    return this.$$.ctx[10];
  }
  set as_item(e) {
    this.$$set({
      as_item: e
    }), h();
  }
  get visible() {
    return this.$$.ctx[11];
  }
  set visible(e) {
    this.$$set({
      visible: e
    }), h();
  }
  get elem_id() {
    return this.$$.ctx[12];
  }
  set elem_id(e) {
    this.$$set({
      elem_id: e
    }), h();
  }
  get elem_classes() {
    return this.$$.ctx[13];
  }
  set elem_classes(e) {
    this.$$set({
      elem_classes: e
    }), h();
  }
  get elem_style() {
    return this.$$.ctx[14];
  }
  set elem_style(e) {
    this.$$set({
      elem_style: e
    }), h();
  }
}
export {
  Rt as default
};
