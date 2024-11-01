import { g as ee, w as x } from "./Index-Kr27gPJZ.js";
const g = window.ms_globals.React, Y = window.ms_globals.React.forwardRef, Q = window.ms_globals.React.useRef, X = window.ms_globals.React.useState, Z = window.ms_globals.React.useEffect, $ = window.ms_globals.React.useMemo, S = window.ms_globals.ReactDOM.createPortal, te = window.ms_globals.antd.Input;
var M = {
  exports: {}
}, R = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var re = g, ne = Symbol.for("react.element"), oe = Symbol.for("react.fragment"), le = Object.prototype.hasOwnProperty, se = re.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, ie = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function W(e, r, n) {
  var l, o = {}, t = null, s = null;
  n !== void 0 && (t = "" + n), r.key !== void 0 && (t = "" + r.key), r.ref !== void 0 && (s = r.ref);
  for (l in r) le.call(r, l) && !ie.hasOwnProperty(l) && (o[l] = r[l]);
  if (e && e.defaultProps) for (l in r = e.defaultProps, r) o[l] === void 0 && (o[l] = r[l]);
  return {
    $$typeof: ne,
    type: e,
    key: t,
    ref: s,
    props: o,
    _owner: se.current
  };
}
R.Fragment = oe;
R.jsx = W;
R.jsxs = W;
M.exports = R;
var m = M.exports;
const {
  SvelteComponent: ae,
  assign: j,
  binding_callbacks: P,
  check_outros: ce,
  children: z,
  claim_element: G,
  claim_space: de,
  component_subscribe: F,
  compute_slots: ue,
  create_slot: fe,
  detach: b,
  element: U,
  empty: A,
  exclude_internal_props: L,
  get_all_dirty_from_scope: _e,
  get_slot_changes: pe,
  group_outros: me,
  init: he,
  insert_hydration: v,
  safe_not_equal: we,
  set_custom_element_data: H,
  space: ge,
  transition_in: C,
  transition_out: O,
  update_slot_base: ye
} = window.__gradio__svelte__internal, {
  beforeUpdate: be,
  getContext: Ee,
  onDestroy: xe,
  setContext: ve
} = window.__gradio__svelte__internal;
function T(e) {
  let r, n;
  const l = (
    /*#slots*/
    e[7].default
  ), o = fe(
    l,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      r = U("svelte-slot"), o && o.c(), this.h();
    },
    l(t) {
      r = G(t, "SVELTE-SLOT", {
        class: !0
      });
      var s = z(r);
      o && o.l(s), s.forEach(b), this.h();
    },
    h() {
      H(r, "class", "svelte-1rt0kpf");
    },
    m(t, s) {
      v(t, r, s), o && o.m(r, null), e[9](r), n = !0;
    },
    p(t, s) {
      o && o.p && (!n || s & /*$$scope*/
      64) && ye(
        o,
        l,
        t,
        /*$$scope*/
        t[6],
        n ? pe(
          l,
          /*$$scope*/
          t[6],
          s,
          null
        ) : _e(
          /*$$scope*/
          t[6]
        ),
        null
      );
    },
    i(t) {
      n || (C(o, t), n = !0);
    },
    o(t) {
      O(o, t), n = !1;
    },
    d(t) {
      t && b(r), o && o.d(t), e[9](null);
    }
  };
}
function Ce(e) {
  let r, n, l, o, t = (
    /*$$slots*/
    e[4].default && T(e)
  );
  return {
    c() {
      r = U("react-portal-target"), n = ge(), t && t.c(), l = A(), this.h();
    },
    l(s) {
      r = G(s, "REACT-PORTAL-TARGET", {
        class: !0
      }), z(r).forEach(b), n = de(s), t && t.l(s), l = A(), this.h();
    },
    h() {
      H(r, "class", "svelte-1rt0kpf");
    },
    m(s, a) {
      v(s, r, a), e[8](r), v(s, n, a), t && t.m(s, a), v(s, l, a), o = !0;
    },
    p(s, [a]) {
      /*$$slots*/
      s[4].default ? t ? (t.p(s, a), a & /*$$slots*/
      16 && C(t, 1)) : (t = T(s), t.c(), C(t, 1), t.m(l.parentNode, l)) : t && (me(), O(t, 1, 1, () => {
        t = null;
      }), ce());
    },
    i(s) {
      o || (C(t), o = !0);
    },
    o(s) {
      O(t), o = !1;
    },
    d(s) {
      s && (b(r), b(n), b(l)), e[8](null), t && t.d(s);
    }
  };
}
function N(e) {
  const {
    svelteInit: r,
    ...n
  } = e;
  return n;
}
function Re(e, r, n) {
  let l, o, {
    $$slots: t = {},
    $$scope: s
  } = r;
  const a = ue(t);
  let {
    svelteInit: i
  } = r;
  const f = x(N(r)), _ = x();
  F(e, _, (d) => n(0, l = d));
  const h = x();
  F(e, h, (d) => n(1, o = d));
  const c = [], u = Ee("$$ms-gr-react-wrapper"), {
    slotKey: p,
    slotIndex: w,
    subSlotIndex: K
  } = ee() || {}, q = i({
    parent: u,
    props: f,
    target: _,
    slot: h,
    slotKey: p,
    slotIndex: w,
    subSlotIndex: K,
    onDestroy(d) {
      c.push(d);
    }
  });
  ve("$$ms-gr-react-wrapper", q), be(() => {
    f.set(N(r));
  }), xe(() => {
    c.forEach((d) => d());
  });
  function V(d) {
    P[d ? "unshift" : "push"](() => {
      l = d, _.set(l);
    });
  }
  function J(d) {
    P[d ? "unshift" : "push"](() => {
      o = d, h.set(o);
    });
  }
  return e.$$set = (d) => {
    n(17, r = j(j({}, r), L(d))), "svelteInit" in d && n(5, i = d.svelteInit), "$$scope" in d && n(6, s = d.$$scope);
  }, r = L(r), [l, o, _, h, a, i, s, t, V, J];
}
class Ie extends ae {
  constructor(r) {
    super(), he(this, r, Re, Ce, we, {
      svelteInit: 5
    });
  }
}
const D = window.ms_globals.rerender, I = window.ms_globals.tree;
function Se(e) {
  function r(n) {
    const l = x(), o = new Ie({
      ...n,
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
          }, a = t.parent ?? I;
          return a.nodes = [...a.nodes, s], D({
            createPortal: S,
            node: I
          }), t.onDestroy(() => {
            a.nodes = a.nodes.filter((i) => i.svelteInstance !== l), D({
              createPortal: S,
              node: I
            });
          }), s;
        },
        ...n.props
      }
    });
    return l.set(o), o;
  }
  return new Promise((n) => {
    window.ms_globals.initializePromise.then(() => {
      n(r);
    });
  });
}
const Oe = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function ke(e) {
  return e ? Object.keys(e).reduce((r, n) => {
    const l = e[n];
    return typeof l == "number" && !Oe.includes(n) ? r[n] = l + "px" : r[n] = l, r;
  }, {}) : {};
}
function k(e) {
  const r = [], n = e.cloneNode(!1);
  if (e._reactElement)
    return r.push(S(g.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: g.Children.toArray(e._reactElement.props.children).map((o) => {
        if (g.isValidElement(o) && o.props.__slot__) {
          const {
            portals: t,
            clonedElement: s
          } = k(o.props.el);
          return g.cloneElement(o, {
            ...o.props,
            el: s,
            children: [...g.Children.toArray(o.props.children), ...t]
          });
        }
        return null;
      })
    }), n)), {
      clonedElement: n,
      portals: r
    };
  Object.keys(e.getEventListeners()).forEach((o) => {
    e.getEventListeners(o).forEach(({
      listener: s,
      type: a,
      useCapture: i
    }) => {
      n.addEventListener(a, s, i);
    });
  });
  const l = Array.from(e.childNodes);
  for (let o = 0; o < l.length; o++) {
    const t = l[o];
    if (t.nodeType === 1) {
      const {
        clonedElement: s,
        portals: a
      } = k(t);
      r.push(...a), n.appendChild(s);
    } else t.nodeType === 3 && n.appendChild(t.cloneNode());
  }
  return {
    clonedElement: n,
    portals: r
  };
}
function je(e, r) {
  e && (typeof e == "function" ? e(r) : e.current = r);
}
const y = Y(({
  slot: e,
  clone: r,
  className: n,
  style: l
}, o) => {
  const t = Q(), [s, a] = X([]);
  return Z(() => {
    var h;
    if (!t.current || !e)
      return;
    let i = e;
    function f() {
      let c = i;
      if (i.tagName.toLowerCase() === "svelte-slot" && i.children.length === 1 && i.children[0] && (c = i.children[0], c.tagName.toLowerCase() === "react-portal-target" && c.children[0] && (c = c.children[0])), je(o, c), n && c.classList.add(...n.split(" ")), l) {
        const u = ke(l);
        Object.keys(u).forEach((p) => {
          c.style[p] = u[p];
        });
      }
    }
    let _ = null;
    if (r && window.MutationObserver) {
      let c = function() {
        var w;
        const {
          portals: u,
          clonedElement: p
        } = k(e);
        i = p, a(u), i.style.display = "contents", f(), (w = t.current) == null || w.appendChild(i);
      };
      c(), _ = new window.MutationObserver(() => {
        var u, p;
        (u = t.current) != null && u.contains(i) && ((p = t.current) == null || p.removeChild(i)), c();
      }), _.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      i.style.display = "contents", f(), (h = t.current) == null || h.appendChild(i);
    return () => {
      var c, u;
      i.style.display = "", (c = t.current) != null && c.contains(i) && ((u = t.current) == null || u.removeChild(i)), _ == null || _.disconnect();
    };
  }, [e, r, n, l, o]), g.createElement("react-child", {
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
function E(e) {
  return $(() => Pe(e), [e]);
}
function Fe(e, r) {
  return e ? /* @__PURE__ */ m.jsx(y, {
    slot: e,
    clone: r == null ? void 0 : r.clone
  }) : null;
}
function B({
  key: e,
  setSlotParams: r,
  slots: n
}, l) {
  return (...o) => (r(e, o), Fe(n[e], {
    clone: !0,
    ...l
  }));
}
const Le = Se(({
  slots: e,
  children: r,
  count: n,
  showCount: l,
  onValueChange: o,
  onChange: t,
  iconRender: s,
  elRef: a,
  setSlotParams: i,
  ...f
}) => {
  const _ = E(n == null ? void 0 : n.strategy), h = E(n == null ? void 0 : n.exceedFormatter), c = E(n == null ? void 0 : n.show), u = E(typeof l == "object" ? l.formatter : void 0), p = E(s);
  return /* @__PURE__ */ m.jsxs(m.Fragment, {
    children: [/* @__PURE__ */ m.jsx("div", {
      style: {
        display: "none"
      },
      children: r
    }), /* @__PURE__ */ m.jsx(te.Password, {
      ...f,
      ref: a,
      onChange: (w) => {
        t == null || t(w), o(w.target.value);
      },
      iconRender: e.iconRender ? B({
        slots: e,
        setSlotParams: i,
        key: "iconRender"
      }) : p,
      showCount: e["showCount.formatter"] ? {
        formatter: B({
          slots: e,
          setSlotParams: i,
          key: "showCount.formatter"
        })
      } : typeof l == "object" && u ? {
        formatter: u
      } : l,
      count: {
        ...n,
        exceedFormatter: h,
        strategy: _,
        show: c || (n == null ? void 0 : n.show)
      },
      addonAfter: e.addonAfter ? /* @__PURE__ */ m.jsx(y, {
        slot: e.addonAfter
      }) : f.addonAfter,
      addonBefore: e.addonBefore ? /* @__PURE__ */ m.jsx(y, {
        slot: e.addonBefore
      }) : f.addonBefore,
      allowClear: e["allowClear.clearIcon"] ? {
        clearIcon: /* @__PURE__ */ m.jsx(y, {
          slot: e["allowClear.clearIcon"]
        })
      } : f.allowClear,
      prefix: e.prefix ? /* @__PURE__ */ m.jsx(y, {
        slot: e.prefix
      }) : f.prefix,
      suffix: e.suffix ? /* @__PURE__ */ m.jsx(y, {
        slot: e.suffix
      }) : f.suffix
    })]
  });
});
export {
  Le as InputPassword,
  Le as default
};
