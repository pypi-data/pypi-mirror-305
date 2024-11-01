import { g as re, w as C } from "./Index-DGPAMwIV.js";
const w = window.ms_globals.React, $ = window.ms_globals.React.forwardRef, ee = window.ms_globals.React.useRef, te = window.ms_globals.React.useState, ne = window.ms_globals.React.useEffect, B = window.ms_globals.React.useMemo, P = window.ms_globals.ReactDOM.createPortal, F = window.ms_globals.antd.Tree;
var V = {
  exports: {}
}, L = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var oe = w, le = Symbol.for("react.element"), se = Symbol.for("react.fragment"), ce = Object.prototype.hasOwnProperty, ie = oe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, ae = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function J(e, n, r) {
  var l, o = {}, t = null, s = null;
  r !== void 0 && (t = "" + r), n.key !== void 0 && (t = "" + n.key), n.ref !== void 0 && (s = n.ref);
  for (l in n) ce.call(n, l) && !ae.hasOwnProperty(l) && (o[l] = n[l]);
  if (e && e.defaultProps) for (l in n = e.defaultProps, n) o[l] === void 0 && (o[l] = n[l]);
  return {
    $$typeof: le,
    type: e,
    key: t,
    ref: s,
    props: o,
    _owner: ie.current
  };
}
L.Fragment = se;
L.jsx = J;
L.jsxs = J;
V.exports = L;
var p = V.exports;
const {
  SvelteComponent: ue,
  assign: A,
  binding_callbacks: M,
  check_outros: de,
  children: Y,
  claim_element: K,
  claim_space: fe,
  component_subscribe: U,
  compute_slots: _e,
  create_slot: he,
  detach: b,
  element: Q,
  empty: W,
  exclude_internal_props: z,
  get_all_dirty_from_scope: me,
  get_slot_changes: pe,
  group_outros: ge,
  init: we,
  insert_hydration: x,
  safe_not_equal: be,
  set_custom_element_data: X,
  space: ye,
  transition_in: O,
  transition_out: N,
  update_slot_base: Ee
} = window.__gradio__svelte__internal, {
  beforeUpdate: ve,
  getContext: Ie,
  onDestroy: Re,
  setContext: Ce
} = window.__gradio__svelte__internal;
function G(e) {
  let n, r;
  const l = (
    /*#slots*/
    e[7].default
  ), o = he(
    l,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      n = Q("svelte-slot"), o && o.c(), this.h();
    },
    l(t) {
      n = K(t, "SVELTE-SLOT", {
        class: !0
      });
      var s = Y(n);
      o && o.l(s), s.forEach(b), this.h();
    },
    h() {
      X(n, "class", "svelte-1rt0kpf");
    },
    m(t, s) {
      x(t, n, s), o && o.m(n, null), e[9](n), r = !0;
    },
    p(t, s) {
      o && o.p && (!r || s & /*$$scope*/
      64) && Ee(
        o,
        l,
        t,
        /*$$scope*/
        t[6],
        r ? pe(
          l,
          /*$$scope*/
          t[6],
          s,
          null
        ) : me(
          /*$$scope*/
          t[6]
        ),
        null
      );
    },
    i(t) {
      r || (O(o, t), r = !0);
    },
    o(t) {
      N(o, t), r = !1;
    },
    d(t) {
      t && b(n), o && o.d(t), e[9](null);
    }
  };
}
function xe(e) {
  let n, r, l, o, t = (
    /*$$slots*/
    e[4].default && G(e)
  );
  return {
    c() {
      n = Q("react-portal-target"), r = ye(), t && t.c(), l = W(), this.h();
    },
    l(s) {
      n = K(s, "REACT-PORTAL-TARGET", {
        class: !0
      }), Y(n).forEach(b), r = fe(s), t && t.l(s), l = W(), this.h();
    },
    h() {
      X(n, "class", "svelte-1rt0kpf");
    },
    m(s, c) {
      x(s, n, c), e[8](n), x(s, r, c), t && t.m(s, c), x(s, l, c), o = !0;
    },
    p(s, [c]) {
      /*$$slots*/
      s[4].default ? t ? (t.p(s, c), c & /*$$slots*/
      16 && O(t, 1)) : (t = G(s), t.c(), O(t, 1), t.m(l.parentNode, l)) : t && (ge(), N(t, 1, 1, () => {
        t = null;
      }), de());
    },
    i(s) {
      o || (O(t), o = !0);
    },
    o(s) {
      N(t), o = !1;
    },
    d(s) {
      s && (b(n), b(r), b(l)), e[8](null), t && t.d(s);
    }
  };
}
function H(e) {
  const {
    svelteInit: n,
    ...r
  } = e;
  return r;
}
function Oe(e, n, r) {
  let l, o, {
    $$slots: t = {},
    $$scope: s
  } = n;
  const c = _e(t);
  let {
    svelteInit: i
  } = n;
  const h = C(H(n)), f = C();
  U(e, f, (u) => r(0, l = u));
  const _ = C();
  U(e, _, (u) => r(1, o = u));
  const a = [], d = Ie("$$ms-gr-react-wrapper"), {
    slotKey: m,
    slotIndex: g,
    subSlotIndex: y
  } = re() || {}, j = i({
    parent: d,
    props: h,
    target: f,
    slot: _,
    slotKey: m,
    slotIndex: g,
    subSlotIndex: y,
    onDestroy(u) {
      a.push(u);
    }
  });
  Ce("$$ms-gr-react-wrapper", j), ve(() => {
    h.set(H(n));
  }), Re(() => {
    a.forEach((u) => u());
  });
  function k(u) {
    M[u ? "unshift" : "push"](() => {
      l = u, f.set(l);
    });
  }
  function S(u) {
    M[u ? "unshift" : "push"](() => {
      o = u, _.set(o);
    });
  }
  return e.$$set = (u) => {
    r(17, n = A(A({}, n), z(u))), "svelteInit" in u && r(5, i = u.svelteInit), "$$scope" in u && r(6, s = u.$$scope);
  }, n = z(n), [l, o, f, _, c, i, s, t, k, S];
}
class Le extends ue {
  constructor(n) {
    super(), we(this, n, Oe, xe, be, {
      svelteInit: 5
    });
  }
}
const q = window.ms_globals.rerender, T = window.ms_globals.tree;
function je(e) {
  function n(r) {
    const l = C(), o = new Le({
      ...r,
      props: {
        svelteInit(t) {
          window.ms_globals.autokey += 1;
          const s = {
            key: window.ms_globals.autokey,
            svelteInstance: l,
            reactComponent: e,
            props: t.props,
            slot: t.slot,
            target: t.target,
            slotIndex: t.slotIndex,
            subSlotIndex: t.subSlotIndex,
            slotKey: t.slotKey,
            nodes: []
          }, c = t.parent ?? T;
          return c.nodes = [...c.nodes, s], q({
            createPortal: P,
            node: T
          }), t.onDestroy(() => {
            c.nodes = c.nodes.filter((i) => i.svelteInstance !== l), q({
              createPortal: P,
              node: T
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
const ke = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Se(e) {
  return e ? Object.keys(e).reduce((n, r) => {
    const l = e[r];
    return typeof l == "number" && !ke.includes(r) ? n[r] = l + "px" : n[r] = l, n;
  }, {}) : {};
}
function D(e) {
  const n = [], r = e.cloneNode(!1);
  if (e._reactElement)
    return n.push(P(w.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: w.Children.toArray(e._reactElement.props.children).map((o) => {
        if (w.isValidElement(o) && o.props.__slot__) {
          const {
            portals: t,
            clonedElement: s
          } = D(o.props.el);
          return w.cloneElement(o, {
            ...o.props,
            el: s,
            children: [...w.Children.toArray(o.props.children), ...t]
          });
        }
        return null;
      })
    }), r)), {
      clonedElement: r,
      portals: n
    };
  Object.keys(e.getEventListeners()).forEach((o) => {
    e.getEventListeners(o).forEach(({
      listener: s,
      type: c,
      useCapture: i
    }) => {
      r.addEventListener(c, s, i);
    });
  });
  const l = Array.from(e.childNodes);
  for (let o = 0; o < l.length; o++) {
    const t = l[o];
    if (t.nodeType === 1) {
      const {
        clonedElement: s,
        portals: c
      } = D(t);
      n.push(...c), r.appendChild(s);
    } else t.nodeType === 3 && r.appendChild(t.cloneNode());
  }
  return {
    clonedElement: r,
    portals: n
  };
}
function Te(e, n) {
  e && (typeof e == "function" ? e(n) : e.current = n);
}
const v = $(({
  slot: e,
  clone: n,
  className: r,
  style: l
}, o) => {
  const t = ee(), [s, c] = te([]);
  return ne(() => {
    var _;
    if (!t.current || !e)
      return;
    let i = e;
    function h() {
      let a = i;
      if (i.tagName.toLowerCase() === "svelte-slot" && i.children.length === 1 && i.children[0] && (a = i.children[0], a.tagName.toLowerCase() === "react-portal-target" && a.children[0] && (a = a.children[0])), Te(o, a), r && a.classList.add(...r.split(" ")), l) {
        const d = Se(l);
        Object.keys(d).forEach((m) => {
          a.style[m] = d[m];
        });
      }
    }
    let f = null;
    if (n && window.MutationObserver) {
      let a = function() {
        var g;
        const {
          portals: d,
          clonedElement: m
        } = D(e);
        i = m, c(d), i.style.display = "contents", h(), (g = t.current) == null || g.appendChild(i);
      };
      a(), f = new window.MutationObserver(() => {
        var d, m;
        (d = t.current) != null && d.contains(i) && ((m = t.current) == null || m.removeChild(i)), a();
      }), f.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      i.style.display = "contents", h(), (_ = t.current) == null || _.appendChild(i);
    return () => {
      var a, d;
      i.style.display = "", (a = t.current) != null && a.contains(i) && ((d = t.current) == null || d.removeChild(i)), f == null || f.disconnect();
    };
  }, [e, n, r, l, o]), w.createElement("react-child", {
    ref: t,
    style: {
      display: "contents"
    }
  }, ...s);
});
function Pe(e) {
  try {
    return typeof e == "string" ? new Function(`return (...args) => (${e})(...args)`)() : void 0;
  } catch {
    return;
  }
}
function I(e) {
  return B(() => Pe(e), [e]);
}
function Ne(e) {
  return Object.keys(e).reduce((n, r) => (e[r] !== void 0 && (n[r] = e[r]), n), {});
}
function Z(e, n) {
  return e.filter(Boolean).map((r) => {
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
      c.forEach((a, d) => {
        o[a] || (o[a] = {}), d !== c.length - 1 && (o = l[a]);
      });
      const i = r.slots[s];
      let h, f, _ = !1;
      i instanceof Element ? h = i : (h = i.el, f = i.callback, _ = i.clone || !1), o[c[c.length - 1]] = h ? f ? (...a) => (f(c[c.length - 1], a), /* @__PURE__ */ p.jsx(v, {
        slot: h,
        clone: _ || (n == null ? void 0 : n.clone)
      })) : /* @__PURE__ */ p.jsx(v, {
        slot: h,
        clone: _ || (n == null ? void 0 : n.clone)
      }) : o[c[c.length - 1]], o = l;
    });
    const t = "children";
    return r[t] && (l[t] = Z(r[t], n)), l;
  });
}
function De(e, n) {
  return e ? /* @__PURE__ */ p.jsx(v, {
    slot: e,
    clone: n == null ? void 0 : n.clone
  }) : null;
}
function R({
  key: e,
  setSlotParams: n,
  slots: r
}, l) {
  return (...o) => (n(e, o), De(r[e], {
    clone: !0,
    ...l
  }));
}
const Ae = je(({
  slots: e,
  filterTreeNode: n,
  treeData: r,
  draggable: l,
  allowDrop: o,
  onCheck: t,
  onSelect: s,
  onExpand: c,
  children: i,
  directory: h,
  slotItems: f,
  setSlotParams: _,
  onLoadData: a,
  ...d
}) => {
  const m = I(n), g = I(l), y = I(typeof l == "object" ? l.nodeDraggable : void 0), j = I(o), k = h ? F.DirectoryTree : F, S = B(() => ({
    ...d,
    treeData: r || Z(f),
    showLine: e["showLine.showLeafIcon"] ? {
      showLeafIcon: R({
        slots: e,
        setSlotParams: _,
        key: "showLine.showLeafIcon"
      })
    } : d.showLine,
    icon: e.icon ? R({
      slots: e,
      setSlotParams: _,
      key: "icon"
    }) : d.icon,
    switcherLoadingIcon: e.switcherLoadingIcon ? /* @__PURE__ */ p.jsx(v, {
      slot: e.switcherLoadingIcon
    }) : d.switcherLoadingIcon,
    switcherIcon: e.switcherIcon ? R({
      slots: e,
      setSlotParams: _,
      key: "switcherIcon"
    }) : d.switcherIcon,
    titleRender: e.titleRender ? R({
      slots: e,
      setSlotParams: _,
      key: "titleRender"
    }) : d.titleRender,
    draggable: e["draggable.icon"] || y ? {
      icon: e["draggable.icon"] ? /* @__PURE__ */ p.jsx(v, {
        slot: e["draggable.icon"]
      }) : typeof l == "object" ? l.icon : void 0,
      nodeDraggable: y
    } : g || l,
    loadData: a
  }), [d, r, f, e, _, y, l, g, a]);
  return /* @__PURE__ */ p.jsxs(p.Fragment, {
    children: [/* @__PURE__ */ p.jsx("div", {
      style: {
        display: "none"
      },
      children: i
    }), /* @__PURE__ */ p.jsx(k, {
      ...Ne(S),
      filterTreeNode: m,
      allowDrop: j,
      onSelect: (u, ...E) => {
        s == null || s(u, ...E);
      },
      onExpand: (u, ...E) => {
        c == null || c(u, ...E);
      },
      onCheck: (u, ...E) => {
        t == null || t(u, ...E);
      }
    })]
  });
});
export {
  Ae as Tree,
  Ae as default
};
