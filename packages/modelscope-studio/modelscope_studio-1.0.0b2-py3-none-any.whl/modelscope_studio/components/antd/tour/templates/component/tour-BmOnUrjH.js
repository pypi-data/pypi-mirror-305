import { g as ee, w as E } from "./Index-Bf20dmfp.js";
const g = window.ms_globals.React, Q = window.ms_globals.React.forwardRef, X = window.ms_globals.React.useRef, Z = window.ms_globals.React.useState, $ = window.ms_globals.React.useEffect, M = window.ms_globals.React.useMemo, S = window.ms_globals.ReactDOM.createPortal, te = window.ms_globals.antd.Tour;
var W = {
  exports: {}
}, x = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var ne = g, re = Symbol.for("react.element"), oe = Symbol.for("react.fragment"), le = Object.prototype.hasOwnProperty, se = ne.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, ce = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function z(n, t, o) {
  var l, r = {}, e = null, s = null;
  o !== void 0 && (e = "" + o), t.key !== void 0 && (e = "" + t.key), t.ref !== void 0 && (s = t.ref);
  for (l in t) le.call(t, l) && !ce.hasOwnProperty(l) && (r[l] = t[l]);
  if (n && n.defaultProps) for (l in t = n.defaultProps, t) r[l] === void 0 && (r[l] = t[l]);
  return {
    $$typeof: re,
    type: n,
    key: e,
    ref: s,
    props: r,
    _owner: se.current
  };
}
x.Fragment = oe;
x.jsx = z;
x.jsxs = z;
W.exports = x;
var h = W.exports;
const {
  SvelteComponent: ie,
  assign: k,
  binding_callbacks: P,
  check_outros: ae,
  children: G,
  claim_element: U,
  claim_space: ue,
  component_subscribe: j,
  compute_slots: de,
  create_slot: fe,
  detach: w,
  element: H,
  empty: T,
  exclude_internal_props: L,
  get_all_dirty_from_scope: _e,
  get_slot_changes: pe,
  group_outros: me,
  init: he,
  insert_hydration: y,
  safe_not_equal: ge,
  set_custom_element_data: q,
  space: we,
  transition_in: v,
  transition_out: C,
  update_slot_base: be
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ee,
  getContext: ye,
  onDestroy: ve,
  setContext: Re
} = window.__gradio__svelte__internal;
function F(n) {
  let t, o;
  const l = (
    /*#slots*/
    n[7].default
  ), r = fe(
    l,
    n,
    /*$$scope*/
    n[6],
    null
  );
  return {
    c() {
      t = H("svelte-slot"), r && r.c(), this.h();
    },
    l(e) {
      t = U(e, "SVELTE-SLOT", {
        class: !0
      });
      var s = G(t);
      r && r.l(s), s.forEach(w), this.h();
    },
    h() {
      q(t, "class", "svelte-1rt0kpf");
    },
    m(e, s) {
      y(e, t, s), r && r.m(t, null), n[9](t), o = !0;
    },
    p(e, s) {
      r && r.p && (!o || s & /*$$scope*/
      64) && be(
        r,
        l,
        e,
        /*$$scope*/
        e[6],
        o ? pe(
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
      o || (v(r, e), o = !0);
    },
    o(e) {
      C(r, e), o = !1;
    },
    d(e) {
      e && w(t), r && r.d(e), n[9](null);
    }
  };
}
function xe(n) {
  let t, o, l, r, e = (
    /*$$slots*/
    n[4].default && F(n)
  );
  return {
    c() {
      t = H("react-portal-target"), o = we(), e && e.c(), l = T(), this.h();
    },
    l(s) {
      t = U(s, "REACT-PORTAL-TARGET", {
        class: !0
      }), G(t).forEach(w), o = ue(s), e && e.l(s), l = T(), this.h();
    },
    h() {
      q(t, "class", "svelte-1rt0kpf");
    },
    m(s, c) {
      y(s, t, c), n[8](t), y(s, o, c), e && e.m(s, c), y(s, l, c), r = !0;
    },
    p(s, [c]) {
      /*$$slots*/
      s[4].default ? e ? (e.p(s, c), c & /*$$slots*/
      16 && v(e, 1)) : (e = F(s), e.c(), v(e, 1), e.m(l.parentNode, l)) : e && (me(), C(e, 1, 1, () => {
        e = null;
      }), ae());
    },
    i(s) {
      r || (v(e), r = !0);
    },
    o(s) {
      C(e), r = !1;
    },
    d(s) {
      s && (w(t), w(o), w(l)), n[8](null), e && e.d(s);
    }
  };
}
function N(n) {
  const {
    svelteInit: t,
    ...o
  } = n;
  return o;
}
function Ie(n, t, o) {
  let l, r, {
    $$slots: e = {},
    $$scope: s
  } = t;
  const c = de(e);
  let {
    svelteInit: i
  } = t;
  const _ = E(N(t)), d = E();
  j(n, d, (u) => o(0, l = u));
  const p = E();
  j(n, p, (u) => o(1, r = u));
  const a = [], f = ye("$$ms-gr-react-wrapper"), {
    slotKey: m,
    slotIndex: b,
    subSlotIndex: V
  } = ee() || {}, J = i({
    parent: f,
    props: _,
    target: d,
    slot: p,
    slotKey: m,
    slotIndex: b,
    subSlotIndex: V,
    onDestroy(u) {
      a.push(u);
    }
  });
  Re("$$ms-gr-react-wrapper", J), Ee(() => {
    _.set(N(t));
  }), ve(() => {
    a.forEach((u) => u());
  });
  function Y(u) {
    P[u ? "unshift" : "push"](() => {
      l = u, d.set(l);
    });
  }
  function K(u) {
    P[u ? "unshift" : "push"](() => {
      r = u, p.set(r);
    });
  }
  return n.$$set = (u) => {
    o(17, t = k(k({}, t), L(u))), "svelteInit" in u && o(5, i = u.svelteInit), "$$scope" in u && o(6, s = u.$$scope);
  }, t = L(t), [l, r, d, p, c, i, s, e, Y, K];
}
class Se extends ie {
  constructor(t) {
    super(), he(this, t, Ie, xe, ge, {
      svelteInit: 5
    });
  }
}
const A = window.ms_globals.rerender, I = window.ms_globals.tree;
function Ce(n) {
  function t(o) {
    const l = E(), r = new Se({
      ...o,
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
          }, c = e.parent ?? I;
          return c.nodes = [...c.nodes, s], A({
            createPortal: S,
            node: I
          }), e.onDestroy(() => {
            c.nodes = c.nodes.filter((i) => i.svelteInstance !== l), A({
              createPortal: S,
              node: I
            });
          }), s;
        },
        ...o.props
      }
    });
    return l.set(r), r;
  }
  return new Promise((o) => {
    window.ms_globals.initializePromise.then(() => {
      o(t);
    });
  });
}
const Oe = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function ke(n) {
  return n ? Object.keys(n).reduce((t, o) => {
    const l = n[o];
    return typeof l == "number" && !Oe.includes(o) ? t[o] = l + "px" : t[o] = l, t;
  }, {}) : {};
}
function O(n) {
  const t = [], o = n.cloneNode(!1);
  if (n._reactElement)
    return t.push(S(g.cloneElement(n._reactElement, {
      ...n._reactElement.props,
      children: g.Children.toArray(n._reactElement.props.children).map((r) => {
        if (g.isValidElement(r) && r.props.__slot__) {
          const {
            portals: e,
            clonedElement: s
          } = O(r.props.el);
          return g.cloneElement(r, {
            ...r.props,
            el: s,
            children: [...g.Children.toArray(r.props.children), ...e]
          });
        }
        return null;
      })
    }), o)), {
      clonedElement: o,
      portals: t
    };
  Object.keys(n.getEventListeners()).forEach((r) => {
    n.getEventListeners(r).forEach(({
      listener: s,
      type: c,
      useCapture: i
    }) => {
      o.addEventListener(c, s, i);
    });
  });
  const l = Array.from(n.childNodes);
  for (let r = 0; r < l.length; r++) {
    const e = l[r];
    if (e.nodeType === 1) {
      const {
        clonedElement: s,
        portals: c
      } = O(e);
      t.push(...c), o.appendChild(s);
    } else e.nodeType === 3 && o.appendChild(e.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function Pe(n, t) {
  n && (typeof n == "function" ? n(t) : n.current = t);
}
const R = Q(({
  slot: n,
  clone: t,
  className: o,
  style: l
}, r) => {
  const e = X(), [s, c] = Z([]);
  return $(() => {
    var p;
    if (!e.current || !n)
      return;
    let i = n;
    function _() {
      let a = i;
      if (i.tagName.toLowerCase() === "svelte-slot" && i.children.length === 1 && i.children[0] && (a = i.children[0], a.tagName.toLowerCase() === "react-portal-target" && a.children[0] && (a = a.children[0])), Pe(r, a), o && a.classList.add(...o.split(" ")), l) {
        const f = ke(l);
        Object.keys(f).forEach((m) => {
          a.style[m] = f[m];
        });
      }
    }
    let d = null;
    if (t && window.MutationObserver) {
      let a = function() {
        var b;
        const {
          portals: f,
          clonedElement: m
        } = O(n);
        i = m, c(f), i.style.display = "contents", _(), (b = e.current) == null || b.appendChild(i);
      };
      a(), d = new window.MutationObserver(() => {
        var f, m;
        (f = e.current) != null && f.contains(i) && ((m = e.current) == null || m.removeChild(i)), a();
      }), d.observe(n, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      i.style.display = "contents", _(), (p = e.current) == null || p.appendChild(i);
    return () => {
      var a, f;
      i.style.display = "", (a = e.current) != null && a.contains(i) && ((f = e.current) == null || f.removeChild(i)), d == null || d.disconnect();
    };
  }, [n, t, o, l, r]), g.createElement("react-child", {
    ref: e,
    style: {
      display: "contents"
    }
  }, ...s);
});
function je(n) {
  try {
    return typeof n == "string" ? new Function(`return (...args) => (${n})(...args)`)() : void 0;
  } catch {
    return;
  }
}
function D(n) {
  return M(() => je(n), [n]);
}
function B(n, t) {
  return n.filter(Boolean).map((o) => {
    if (typeof o != "object")
      return o;
    const l = {
      ...o.props
    };
    let r = l;
    Object.keys(o.slots).forEach((s) => {
      if (!o.slots[s] || !(o.slots[s] instanceof Element) && !o.slots[s].el)
        return;
      const c = s.split(".");
      c.forEach((a, f) => {
        r[a] || (r[a] = {}), f !== c.length - 1 && (r = l[a]);
      });
      const i = o.slots[s];
      let _, d, p = !1;
      i instanceof Element ? _ = i : (_ = i.el, d = i.callback, p = i.clone || !1), r[c[c.length - 1]] = _ ? d ? (...a) => (d(c[c.length - 1], a), /* @__PURE__ */ h.jsx(R, {
        slot: _,
        clone: p || (t == null ? void 0 : t.clone)
      })) : /* @__PURE__ */ h.jsx(R, {
        slot: _,
        clone: p || (t == null ? void 0 : t.clone)
      }) : r[c[c.length - 1]], r = l;
    });
    const e = "children";
    return o[e] && (l[e] = B(o[e], t)), l;
  });
}
function Te(n, t) {
  return n ? /* @__PURE__ */ h.jsx(R, {
    slot: n,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function Le({
  key: n,
  setSlotParams: t,
  slots: o
}, l) {
  return (...r) => (t(n, r), Te(o[n], {
    clone: !0,
    ...l
  }));
}
const Ne = Ce(({
  slots: n,
  steps: t,
  slotItems: o,
  children: l,
  onChange: r,
  onClose: e,
  getPopupContainer: s,
  setSlotParams: c,
  indicatorsRender: i,
  ..._
}) => {
  const d = D(s), p = D(i);
  return /* @__PURE__ */ h.jsxs(h.Fragment, {
    children: [/* @__PURE__ */ h.jsx("div", {
      style: {
        display: "none"
      },
      children: l
    }), /* @__PURE__ */ h.jsx(te, {
      ..._,
      steps: M(() => t || B(o), [t, o]),
      onChange: (a) => {
        r == null || r(a);
      },
      closeIcon: n.closeIcon ? /* @__PURE__ */ h.jsx(R, {
        slot: n.closeIcon
      }) : _.closeIcon,
      indicatorsRender: n.indicatorsRender ? Le({
        slots: n,
        setSlotParams: c,
        key: "indicatorsRender"
      }) : p,
      getPopupContainer: d,
      onClose: (a, ...f) => {
        e == null || e(a, ...f);
      }
    })]
  });
});
export {
  Ne as Tour,
  Ne as default
};
