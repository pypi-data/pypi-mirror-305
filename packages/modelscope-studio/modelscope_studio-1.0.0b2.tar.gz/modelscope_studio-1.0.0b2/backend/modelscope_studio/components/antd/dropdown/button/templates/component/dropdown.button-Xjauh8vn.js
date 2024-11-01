import { g as ne, w as v, d as re, a as y } from "./Index-CW230bWe.js";
const g = window.ms_globals.React, R = window.ms_globals.React.useMemo, U = window.ms_globals.React.useState, H = window.ms_globals.React.useEffect, ee = window.ms_globals.React.forwardRef, te = window.ms_globals.React.useRef, P = window.ms_globals.ReactDOM.createPortal, oe = window.ms_globals.antd.Dropdown;
var V = {
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
var se = g, le = Symbol.for("react.element"), ce = Symbol.for("react.fragment"), ie = Object.prototype.hasOwnProperty, ue = se.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, ae = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function q(n, t, r) {
  var l, o = {}, e = null, s = null;
  r !== void 0 && (e = "" + r), t.key !== void 0 && (e = "" + t.key), t.ref !== void 0 && (s = t.ref);
  for (l in t) ie.call(t, l) && !ae.hasOwnProperty(l) && (o[l] = t[l]);
  if (n && n.defaultProps) for (l in t = n.defaultProps, t) o[l] === void 0 && (o[l] = t[l]);
  return {
    $$typeof: le,
    type: n,
    key: e,
    ref: s,
    props: o,
    _owner: ue.current
  };
}
C.Fragment = ce;
C.jsx = q;
C.jsxs = q;
V.exports = C;
var b = V.exports;
const {
  SvelteComponent: de,
  assign: A,
  binding_callbacks: F,
  check_outros: fe,
  children: J,
  claim_element: Y,
  claim_space: pe,
  component_subscribe: N,
  compute_slots: _e,
  create_slot: me,
  detach: w,
  element: K,
  empty: D,
  exclude_internal_props: B,
  get_all_dirty_from_scope: he,
  get_slot_changes: ge,
  group_outros: we,
  init: be,
  insert_hydration: I,
  safe_not_equal: ye,
  set_custom_element_data: Q,
  space: Ee,
  transition_in: x,
  transition_out: T,
  update_slot_base: ve
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ie,
  getContext: xe,
  onDestroy: Re,
  setContext: Ce
} = window.__gradio__svelte__internal;
function M(n) {
  let t, r;
  const l = (
    /*#slots*/
    n[7].default
  ), o = me(
    l,
    n,
    /*$$scope*/
    n[6],
    null
  );
  return {
    c() {
      t = K("svelte-slot"), o && o.c(), this.h();
    },
    l(e) {
      t = Y(e, "SVELTE-SLOT", {
        class: !0
      });
      var s = J(t);
      o && o.l(s), s.forEach(w), this.h();
    },
    h() {
      Q(t, "class", "svelte-1rt0kpf");
    },
    m(e, s) {
      I(e, t, s), o && o.m(t, null), n[9](t), r = !0;
    },
    p(e, s) {
      o && o.p && (!r || s & /*$$scope*/
      64) && ve(
        o,
        l,
        e,
        /*$$scope*/
        e[6],
        r ? ge(
          l,
          /*$$scope*/
          e[6],
          s,
          null
        ) : he(
          /*$$scope*/
          e[6]
        ),
        null
      );
    },
    i(e) {
      r || (x(o, e), r = !0);
    },
    o(e) {
      T(o, e), r = !1;
    },
    d(e) {
      e && w(t), o && o.d(e), n[9](null);
    }
  };
}
function Se(n) {
  let t, r, l, o, e = (
    /*$$slots*/
    n[4].default && M(n)
  );
  return {
    c() {
      t = K("react-portal-target"), r = Ee(), e && e.c(), l = D(), this.h();
    },
    l(s) {
      t = Y(s, "REACT-PORTAL-TARGET", {
        class: !0
      }), J(t).forEach(w), r = pe(s), e && e.l(s), l = D(), this.h();
    },
    h() {
      Q(t, "class", "svelte-1rt0kpf");
    },
    m(s, c) {
      I(s, t, c), n[8](t), I(s, r, c), e && e.m(s, c), I(s, l, c), o = !0;
    },
    p(s, [c]) {
      /*$$slots*/
      s[4].default ? e ? (e.p(s, c), c & /*$$slots*/
      16 && x(e, 1)) : (e = M(s), e.c(), x(e, 1), e.m(l.parentNode, l)) : e && (we(), T(e, 1, 1, () => {
        e = null;
      }), fe());
    },
    i(s) {
      o || (x(e), o = !0);
    },
    o(s) {
      T(e), o = !1;
    },
    d(s) {
      s && (w(t), w(r), w(l)), n[8](null), e && e.d(s);
    }
  };
}
function W(n) {
  const {
    svelteInit: t,
    ...r
  } = n;
  return r;
}
function Oe(n, t, r) {
  let l, o, {
    $$slots: e = {},
    $$scope: s
  } = t;
  const c = _e(e);
  let {
    svelteInit: i
  } = t;
  const _ = v(W(t)), f = v();
  N(n, f, (a) => r(0, l = a));
  const p = v();
  N(n, p, (a) => r(1, o = a));
  const u = [], d = xe("$$ms-gr-react-wrapper"), {
    slotKey: m,
    slotIndex: h,
    subSlotIndex: S
  } = ne() || {}, O = i({
    parent: d,
    props: _,
    target: f,
    slot: p,
    slotKey: m,
    slotIndex: h,
    subSlotIndex: S,
    onDestroy(a) {
      u.push(a);
    }
  });
  Ce("$$ms-gr-react-wrapper", O), Ie(() => {
    _.set(W(t));
  }), Re(() => {
    u.forEach((a) => a());
  });
  function Z(a) {
    F[a ? "unshift" : "push"](() => {
      l = a, f.set(l);
    });
  }
  function $(a) {
    F[a ? "unshift" : "push"](() => {
      o = a, p.set(o);
    });
  }
  return n.$$set = (a) => {
    r(17, t = A(A({}, t), B(a))), "svelteInit" in a && r(5, i = a.svelteInit), "$$scope" in a && r(6, s = a.$$scope);
  }, t = B(t), [l, o, f, p, c, i, s, e, Z, $];
}
class ke extends de {
  constructor(t) {
    super(), be(this, t, Oe, Se, ye, {
      svelteInit: 5
    });
  }
}
const z = window.ms_globals.rerender, k = window.ms_globals.tree;
function je(n) {
  function t(r) {
    const l = v(), o = new ke({
      ...r,
      props: {
        svelteInit(e) {
          window.ms_globals.autokey += 1;
          const s = {
            key: window.ms_globals.autokey,
            svelteInstance: l,
            reactComponent: n,
            props: e.props,
            slot: e.slot,
            target: e.target,
            slotIndex: e.slotIndex,
            subSlotIndex: e.subSlotIndex,
            slotKey: e.slotKey,
            nodes: []
          }, c = e.parent ?? k;
          return c.nodes = [...c.nodes, s], z({
            createPortal: P,
            node: k
          }), e.onDestroy(() => {
            c.nodes = c.nodes.filter((i) => i.svelteInstance !== l), z({
              createPortal: P,
              node: k
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
      r(t);
    });
  });
}
function Pe(n) {
  const [t, r] = U(() => y(n));
  return H(() => {
    let l = !0;
    return n.subscribe((e) => {
      l && (l = !1, e === t) || r(e);
    });
  }, [n]), t;
}
function Te(n) {
  const t = R(() => re(n, (r) => r), [n]);
  return Pe(t);
}
const Le = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Ae(n) {
  return n ? Object.keys(n).reduce((t, r) => {
    const l = n[r];
    return typeof l == "number" && !Le.includes(r) ? t[r] = l + "px" : t[r] = l, t;
  }, {}) : {};
}
function L(n) {
  const t = [], r = n.cloneNode(!1);
  if (n._reactElement)
    return t.push(P(g.cloneElement(n._reactElement, {
      ...n._reactElement.props,
      children: g.Children.toArray(n._reactElement.props.children).map((o) => {
        if (g.isValidElement(o) && o.props.__slot__) {
          const {
            portals: e,
            clonedElement: s
          } = L(o.props.el);
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
      portals: t
    };
  Object.keys(n.getEventListeners()).forEach((o) => {
    n.getEventListeners(o).forEach(({
      listener: s,
      type: c,
      useCapture: i
    }) => {
      r.addEventListener(c, s, i);
    });
  });
  const l = Array.from(n.childNodes);
  for (let o = 0; o < l.length; o++) {
    const e = l[o];
    if (e.nodeType === 1) {
      const {
        clonedElement: s,
        portals: c
      } = L(e);
      t.push(...c), r.appendChild(s);
    } else e.nodeType === 3 && r.appendChild(e.cloneNode());
  }
  return {
    clonedElement: r,
    portals: t
  };
}
function Fe(n, t) {
  n && (typeof n == "function" ? n(t) : n.current = t);
}
const E = ee(({
  slot: n,
  clone: t,
  className: r,
  style: l
}, o) => {
  const e = te(), [s, c] = U([]);
  return H(() => {
    var p;
    if (!e.current || !n)
      return;
    let i = n;
    function _() {
      let u = i;
      if (i.tagName.toLowerCase() === "svelte-slot" && i.children.length === 1 && i.children[0] && (u = i.children[0], u.tagName.toLowerCase() === "react-portal-target" && u.children[0] && (u = u.children[0])), Fe(o, u), r && u.classList.add(...r.split(" ")), l) {
        const d = Ae(l);
        Object.keys(d).forEach((m) => {
          u.style[m] = d[m];
        });
      }
    }
    let f = null;
    if (t && window.MutationObserver) {
      let u = function() {
        var h;
        const {
          portals: d,
          clonedElement: m
        } = L(n);
        i = m, c(d), i.style.display = "contents", _(), (h = e.current) == null || h.appendChild(i);
      };
      u(), f = new window.MutationObserver(() => {
        var d, m;
        (d = e.current) != null && d.contains(i) && ((m = e.current) == null || m.removeChild(i)), u();
      }), f.observe(n, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      i.style.display = "contents", _(), (p = e.current) == null || p.appendChild(i);
    return () => {
      var u, d;
      i.style.display = "", (u = e.current) != null && u.contains(i) && ((d = e.current) == null || d.removeChild(i)), f == null || f.disconnect();
    };
  }, [n, t, r, l, o]), g.createElement("react-child", {
    ref: e,
    style: {
      display: "contents"
    }
  }, ...s);
});
function Ne(n) {
  try {
    return typeof n == "string" ? new Function(`return (...args) => (${n})(...args)`)() : void 0;
  } catch {
    return;
  }
}
function j(n) {
  return R(() => Ne(n), [n]);
}
function De(n, t) {
  const r = R(() => g.Children.toArray(n).filter((e) => e.props.node && t === e.props.nodeSlotKey).sort((e, s) => {
    if (e.props.node.slotIndex && s.props.node.slotIndex) {
      const c = y(e.props.node.slotIndex) || 0, i = y(s.props.node.slotIndex) || 0;
      return c - i === 0 && e.props.node.subSlotIndex && s.props.node.subSlotIndex ? (y(e.props.node.subSlotIndex) || 0) - (y(s.props.node.subSlotIndex) || 0) : c - i;
    }
    return 0;
  }).map((e) => e.props.node.target), [n, t]);
  return Te(r);
}
function X(n, t) {
  return n.filter(Boolean).map((r) => {
    if (typeof r != "object")
      return r;
    const l = {
      ...r.props
    };
    let o = l;
    Object.keys(r.slots).forEach((s) => {
      if (!r.slots[s] || !(r.slots[s] instanceof Element) && !r.slots[s].el)
        return;
      const c = s.split(".");
      c.forEach((u, d) => {
        o[u] || (o[u] = {}), d !== c.length - 1 && (o = l[u]);
      });
      const i = r.slots[s];
      let _, f, p = !1;
      i instanceof Element ? _ = i : (_ = i.el, f = i.callback, p = i.clone || !1), o[c[c.length - 1]] = _ ? f ? (...u) => (f(c[c.length - 1], u), /* @__PURE__ */ b.jsx(E, {
        slot: _,
        clone: p || (t == null ? void 0 : t.clone)
      })) : /* @__PURE__ */ b.jsx(E, {
        slot: _,
        clone: p || (t == null ? void 0 : t.clone)
      }) : o[c[c.length - 1]], o = l;
    });
    const e = "children";
    return r[e] && (l[e] = X(r[e], t)), l;
  });
}
function Be(n, t) {
  return n ? /* @__PURE__ */ b.jsx(E, {
    slot: n,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function G({
  key: n,
  setSlotParams: t,
  slots: r
}, l) {
  return (...o) => (t(n, o), Be(r[n], {
    clone: !0,
    ...l
  }));
}
const We = je(({
  getPopupContainer: n,
  slots: t,
  menuItems: r,
  children: l,
  dropdownRender: o,
  buttonsRender: e,
  setSlotParams: s,
  ...c
}) => {
  var u, d, m;
  const i = j(n), _ = j(o), f = j(e), p = De(l, "buttonsRender");
  return /* @__PURE__ */ b.jsx(oe.Button, {
    ...c,
    buttonsRender: p.length ? (...h) => (s("buttonsRender", h), p.map((S, O) => /* @__PURE__ */ b.jsx(E, {
      slot: S
    }, O))) : f,
    menu: {
      ...c.menu,
      items: R(() => {
        var h;
        return ((h = c.menu) == null ? void 0 : h.items) || X(r);
      }, [r, (u = c.menu) == null ? void 0 : u.items]),
      expandIcon: t["menu.expandIcon"] ? G({
        slots: t,
        setSlotParams: s,
        key: "menu.expandIcon"
      }, {
        clone: !0
      }) : (d = c.menu) == null ? void 0 : d.expandIcon,
      overflowedIndicator: t["menu.overflowedIndicator"] ? /* @__PURE__ */ b.jsx(E, {
        slot: t["menu.overflowedIndicator"]
      }) : (m = c.menu) == null ? void 0 : m.overflowedIndicator
    },
    getPopupContainer: i,
    dropdownRender: t.dropdownRender ? G({
      slots: t,
      setSlotParams: s,
      key: "dropdownRender"
    }) : _
  });
});
export {
  We as DropdownButton,
  We as default
};
