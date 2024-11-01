import { g as ee, w as v } from "./Index-Bocmusiw.js";
const g = window.ms_globals.React, Q = window.ms_globals.React.forwardRef, X = window.ms_globals.React.useRef, Z = window.ms_globals.React.useState, $ = window.ms_globals.React.useEffect, z = window.ms_globals.React.useMemo, R = window.ms_globals.ReactDOM.createPortal, te = window.ms_globals.antd.Tabs;
var D = {
  exports: {}
}, C = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var ne = g, re = Symbol.for("react.element"), oe = Symbol.for("react.fragment"), le = Object.prototype.hasOwnProperty, se = ne.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, ae = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function M(t, n, r) {
  var l, o = {}, e = null, s = null;
  r !== void 0 && (e = "" + r), n.key !== void 0 && (e = "" + n.key), n.ref !== void 0 && (s = n.ref);
  for (l in n) le.call(n, l) && !ae.hasOwnProperty(l) && (o[l] = n[l]);
  if (t && t.defaultProps) for (l in n = t.defaultProps, n) o[l] === void 0 && (o[l] = n[l]);
  return {
    $$typeof: re,
    type: t,
    key: e,
    ref: s,
    props: o,
    _owner: se.current
  };
}
C.Fragment = oe;
C.jsx = M;
C.jsxs = M;
D.exports = C;
var h = D.exports;
const {
  SvelteComponent: ce,
  assign: P,
  binding_callbacks: k,
  check_outros: ie,
  children: U,
  claim_element: W,
  claim_space: ue,
  component_subscribe: T,
  compute_slots: de,
  create_slot: fe,
  detach: E,
  element: G,
  empty: B,
  exclude_internal_props: L,
  get_all_dirty_from_scope: _e,
  get_slot_changes: pe,
  group_outros: he,
  init: be,
  insert_hydration: x,
  safe_not_equal: me,
  set_custom_element_data: H,
  space: ge,
  transition_in: y,
  transition_out: O,
  update_slot_base: Ee
} = window.__gradio__svelte__internal, {
  beforeUpdate: we,
  getContext: ve,
  onDestroy: xe,
  setContext: ye
} = window.__gradio__svelte__internal;
function F(t) {
  let n, r;
  const l = (
    /*#slots*/
    t[7].default
  ), o = fe(
    l,
    t,
    /*$$scope*/
    t[6],
    null
  );
  return {
    c() {
      n = G("svelte-slot"), o && o.c(), this.h();
    },
    l(e) {
      n = W(e, "SVELTE-SLOT", {
        class: !0
      });
      var s = U(n);
      o && o.l(s), s.forEach(E), this.h();
    },
    h() {
      H(n, "class", "svelte-1rt0kpf");
    },
    m(e, s) {
      x(e, n, s), o && o.m(n, null), t[9](n), r = !0;
    },
    p(e, s) {
      o && o.p && (!r || s & /*$$scope*/
      64) && Ee(
        o,
        l,
        e,
        /*$$scope*/
        e[6],
        r ? pe(
          l,
          /*$$scope*/
          e[6],
          s,
          null
        ) : _e(
          /*$$scope*/
          e[6]
        ),
        null
      );
    },
    i(e) {
      r || (y(o, e), r = !0);
    },
    o(e) {
      O(o, e), r = !1;
    },
    d(e) {
      e && E(n), o && o.d(e), t[9](null);
    }
  };
}
function Ce(t) {
  let n, r, l, o, e = (
    /*$$slots*/
    t[4].default && F(t)
  );
  return {
    c() {
      n = G("react-portal-target"), r = ge(), e && e.c(), l = B(), this.h();
    },
    l(s) {
      n = W(s, "REACT-PORTAL-TARGET", {
        class: !0
      }), U(n).forEach(E), r = ue(s), e && e.l(s), l = B(), this.h();
    },
    h() {
      H(n, "class", "svelte-1rt0kpf");
    },
    m(s, a) {
      x(s, n, a), t[8](n), x(s, r, a), e && e.m(s, a), x(s, l, a), o = !0;
    },
    p(s, [a]) {
      /*$$slots*/
      s[4].default ? e ? (e.p(s, a), a & /*$$slots*/
      16 && y(e, 1)) : (e = F(s), e.c(), y(e, 1), e.m(l.parentNode, l)) : e && (he(), O(e, 1, 1, () => {
        e = null;
      }), ie());
    },
    i(s) {
      o || (y(e), o = !0);
    },
    o(s) {
      O(e), o = !1;
    },
    d(s) {
      s && (E(n), E(r), E(l)), t[8](null), e && e.d(s);
    }
  };
}
function N(t) {
  const {
    svelteInit: n,
    ...r
  } = t;
  return r;
}
function Ie(t, n, r) {
  let l, o, {
    $$slots: e = {},
    $$scope: s
  } = n;
  const a = de(e);
  let {
    svelteInit: c
  } = n;
  const f = v(N(n)), d = v();
  T(t, d, (u) => r(0, l = u));
  const p = v();
  T(t, p, (u) => r(1, o = u));
  const i = [], _ = ve("$$ms-gr-react-wrapper"), {
    slotKey: b,
    slotIndex: w,
    subSlotIndex: V
  } = ee() || {}, J = c({
    parent: _,
    props: f,
    target: d,
    slot: p,
    slotKey: b,
    slotIndex: w,
    subSlotIndex: V,
    onDestroy(u) {
      i.push(u);
    }
  });
  ye("$$ms-gr-react-wrapper", J), we(() => {
    f.set(N(n));
  }), xe(() => {
    i.forEach((u) => u());
  });
  function Y(u) {
    k[u ? "unshift" : "push"](() => {
      l = u, d.set(l);
    });
  }
  function K(u) {
    k[u ? "unshift" : "push"](() => {
      o = u, p.set(o);
    });
  }
  return t.$$set = (u) => {
    r(17, n = P(P({}, n), L(u))), "svelteInit" in u && r(5, c = u.svelteInit), "$$scope" in u && r(6, s = u.$$scope);
  }, n = L(n), [l, o, d, p, a, c, s, e, Y, K];
}
class Se extends ce {
  constructor(n) {
    super(), be(this, n, Ie, Ce, me, {
      svelteInit: 5
    });
  }
}
const A = window.ms_globals.rerender, I = window.ms_globals.tree;
function Re(t) {
  function n(r) {
    const l = v(), o = new Se({
      ...r,
      props: {
        svelteInit(e) {
          window.ms_globals.autokey += 1;
          const s = {
            key: window.ms_globals.autokey,
            svelteInstance: l,
            reactComponent: t,
            props: e.props,
            slot: e.slot,
            target: e.target,
            slotIndex: e.slotIndex,
            subSlotIndex: e.subSlotIndex,
            slotKey: e.slotKey,
            nodes: []
          }, a = e.parent ?? I;
          return a.nodes = [...a.nodes, s], A({
            createPortal: R,
            node: I
          }), e.onDestroy(() => {
            a.nodes = a.nodes.filter((c) => c.svelteInstance !== l), A({
              createPortal: R,
              node: I
            });
          }), s;
        },
        ...r.props
      }
    });
    return l.set(o), o;
  }
  return new Promise((r) => {
    window.ms_globals.initializePromise.then(() => {
      r(n);
    });
  });
}
const Oe = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function je(t) {
  return t ? Object.keys(t).reduce((n, r) => {
    const l = t[r];
    return typeof l == "number" && !Oe.includes(r) ? n[r] = l + "px" : n[r] = l, n;
  }, {}) : {};
}
function j(t) {
  const n = [], r = t.cloneNode(!1);
  if (t._reactElement)
    return n.push(R(g.cloneElement(t._reactElement, {
      ...t._reactElement.props,
      children: g.Children.toArray(t._reactElement.props.children).map((o) => {
        if (g.isValidElement(o) && o.props.__slot__) {
          const {
            portals: e,
            clonedElement: s
          } = j(o.props.el);
          return g.cloneElement(o, {
            ...o.props,
            el: s,
            children: [...g.Children.toArray(o.props.children), ...e]
          });
        }
        return null;
      })
    }), r)), {
      clonedElement: r,
      portals: n
    };
  Object.keys(t.getEventListeners()).forEach((o) => {
    t.getEventListeners(o).forEach(({
      listener: s,
      type: a,
      useCapture: c
    }) => {
      r.addEventListener(a, s, c);
    });
  });
  const l = Array.from(t.childNodes);
  for (let o = 0; o < l.length; o++) {
    const e = l[o];
    if (e.nodeType === 1) {
      const {
        clonedElement: s,
        portals: a
      } = j(e);
      n.push(...a), r.appendChild(s);
    } else e.nodeType === 3 && r.appendChild(e.cloneNode());
  }
  return {
    clonedElement: r,
    portals: n
  };
}
function Pe(t, n) {
  t && (typeof t == "function" ? t(n) : t.current = n);
}
const m = Q(({
  slot: t,
  clone: n,
  className: r,
  style: l
}, o) => {
  const e = X(), [s, a] = Z([]);
  return $(() => {
    var p;
    if (!e.current || !t)
      return;
    let c = t;
    function f() {
      let i = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (i = c.children[0], i.tagName.toLowerCase() === "react-portal-target" && i.children[0] && (i = i.children[0])), Pe(o, i), r && i.classList.add(...r.split(" ")), l) {
        const _ = je(l);
        Object.keys(_).forEach((b) => {
          i.style[b] = _[b];
        });
      }
    }
    let d = null;
    if (n && window.MutationObserver) {
      let i = function() {
        var w;
        const {
          portals: _,
          clonedElement: b
        } = j(t);
        c = b, a(_), c.style.display = "contents", f(), (w = e.current) == null || w.appendChild(c);
      };
      i(), d = new window.MutationObserver(() => {
        var _, b;
        (_ = e.current) != null && _.contains(c) && ((b = e.current) == null || b.removeChild(c)), i();
      }), d.observe(t, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", f(), (p = e.current) == null || p.appendChild(c);
    return () => {
      var i, _;
      c.style.display = "", (i = e.current) != null && i.contains(c) && ((_ = e.current) == null || _.removeChild(c)), d == null || d.disconnect();
    };
  }, [t, n, r, l, o]), g.createElement("react-child", {
    ref: e,
    style: {
      display: "contents"
    }
  }, ...s);
});
function ke(t) {
  try {
    return typeof t == "string" ? new Function(`return (...args) => (${t})(...args)`)() : void 0;
  } catch {
    return;
  }
}
function S(t) {
  return z(() => ke(t), [t]);
}
function Te(t) {
  return Object.keys(t).reduce((n, r) => (t[r] !== void 0 && (n[r] = t[r]), n), {});
}
function q(t, n) {
  return t.filter(Boolean).map((r) => {
    if (typeof r != "object")
      return r;
    const l = {
      ...r.props
    };
    let o = l;
    Object.keys(r.slots).forEach((s) => {
      if (!r.slots[s] || !(r.slots[s] instanceof Element) && !r.slots[s].el)
        return;
      const a = s.split(".");
      a.forEach((i, _) => {
        o[i] || (o[i] = {}), _ !== a.length - 1 && (o = l[i]);
      });
      const c = r.slots[s];
      let f, d, p = !1;
      c instanceof Element ? f = c : (f = c.el, d = c.callback, p = c.clone || !1), o[a[a.length - 1]] = f ? d ? (...i) => (d(a[a.length - 1], i), /* @__PURE__ */ h.jsx(m, {
        slot: f,
        clone: p || (n == null ? void 0 : n.clone)
      })) : /* @__PURE__ */ h.jsx(m, {
        slot: f,
        clone: p || (n == null ? void 0 : n.clone)
      }) : o[a[a.length - 1]], o = l;
    });
    const e = "children";
    return r[e] && (l[e] = q(r[e], n)), l;
  });
}
function Be(t, n) {
  return t ? /* @__PURE__ */ h.jsx(m, {
    slot: t,
    clone: n == null ? void 0 : n.clone
  }) : null;
}
function Le({
  key: t,
  setSlotParams: n,
  slots: r
}, l) {
  return (...o) => (n(t, o), Be(r[t], {
    clone: !0,
    ...l
  }));
}
const Ne = Re(({
  slots: t,
  indicator: n,
  items: r,
  onChange: l,
  slotItems: o,
  more: e,
  children: s,
  renderTabBar: a,
  setSlotParams: c,
  ...f
}) => {
  const d = S(n == null ? void 0 : n.size), p = S(e == null ? void 0 : e.getPopupContainer), i = S(a);
  return /* @__PURE__ */ h.jsxs(h.Fragment, {
    children: [/* @__PURE__ */ h.jsx("div", {
      style: {
        display: "none"
      },
      children: s
    }), /* @__PURE__ */ h.jsx(te, {
      ...f,
      indicator: d ? {
        ...n,
        size: d
      } : n,
      renderTabBar: t.renderTabBar ? Le({
        slots: t,
        setSlotParams: c,
        key: "renderTabBar"
      }) : i,
      items: z(() => r || q(o), [r, o]),
      more: Te({
        ...e || {},
        getPopupContainer: p || (e == null ? void 0 : e.getPopupContainer),
        icon: t["more.icon"] ? /* @__PURE__ */ h.jsx(m, {
          slot: t["more.icon"]
        }) : e == null ? void 0 : e.icon
      }),
      tabBarExtraContent: t.tabBarExtraContent ? /* @__PURE__ */ h.jsx(m, {
        slot: t.tabBarExtraContent
      }) : t["tabBarExtraContent.left"] || t["tabBarExtraContent.right"] ? {
        left: t["tabBarExtraContent.left"] ? /* @__PURE__ */ h.jsx(m, {
          slot: t["tabBarExtraContent.left"]
        }) : void 0,
        right: t["tabBarExtraContent.right"] ? /* @__PURE__ */ h.jsx(m, {
          slot: t["tabBarExtraContent.right"]
        }) : void 0
      } : f.tabBarExtraContent,
      addIcon: t.addIcon ? /* @__PURE__ */ h.jsx(m, {
        slot: t.addIcon
      }) : f.addIcon,
      removeIcon: t.removeIcon ? /* @__PURE__ */ h.jsx(m, {
        slot: t.removeIcon
      }) : f.removeIcon,
      onChange: (_) => {
        l == null || l(_);
      }
    })]
  });
});
export {
  Ne as Tabs,
  Ne as default
};
