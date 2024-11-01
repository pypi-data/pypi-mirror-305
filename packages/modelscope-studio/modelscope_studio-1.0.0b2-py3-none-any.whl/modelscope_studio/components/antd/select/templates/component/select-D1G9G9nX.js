import { g as oe, w as R } from "./Index-BS7BGbdp.js";
const y = window.ms_globals.React, te = window.ms_globals.React.forwardRef, ne = window.ms_globals.React.useRef, re = window.ms_globals.React.useState, le = window.ms_globals.React.useEffect, q = window.ms_globals.React.useMemo, P = window.ms_globals.ReactDOM.createPortal, ce = window.ms_globals.antd.Select;
var B = {
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
var se = y, ae = Symbol.for("react.element"), ie = Symbol.for("react.fragment"), de = Object.prototype.hasOwnProperty, ue = se.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, fe = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function V(e, t, l) {
  var o, r = {}, n = null, c = null;
  l !== void 0 && (n = "" + l), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (c = t.ref);
  for (o in t) de.call(t, o) && !fe.hasOwnProperty(o) && (r[o] = t[o]);
  if (e && e.defaultProps) for (o in t = e.defaultProps, t) r[o] === void 0 && (r[o] = t[o]);
  return {
    $$typeof: ae,
    type: e,
    key: n,
    ref: c,
    props: r,
    _owner: ue.current
  };
}
C.Fragment = ie;
C.jsx = V;
C.jsxs = V;
B.exports = C;
var g = B.exports;
const {
  SvelteComponent: _e,
  assign: A,
  binding_callbacks: D,
  check_outros: me,
  children: J,
  claim_element: Y,
  claim_space: he,
  component_subscribe: M,
  compute_slots: pe,
  create_slot: ge,
  detach: E,
  element: K,
  empty: W,
  exclude_internal_props: z,
  get_all_dirty_from_scope: we,
  get_slot_changes: be,
  group_outros: ye,
  init: Ee,
  insert_hydration: v,
  safe_not_equal: Ie,
  set_custom_element_data: Q,
  space: Re,
  transition_in: x,
  transition_out: T,
  update_slot_base: ve
} = window.__gradio__svelte__internal, {
  beforeUpdate: xe,
  getContext: Ce,
  onDestroy: Se,
  setContext: ke
} = window.__gradio__svelte__internal;
function G(e) {
  let t, l;
  const o = (
    /*#slots*/
    e[7].default
  ), r = ge(
    o,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = K("svelte-slot"), r && r.c(), this.h();
    },
    l(n) {
      t = Y(n, "SVELTE-SLOT", {
        class: !0
      });
      var c = J(t);
      r && r.l(c), c.forEach(E), this.h();
    },
    h() {
      Q(t, "class", "svelte-1rt0kpf");
    },
    m(n, c) {
      v(n, t, c), r && r.m(t, null), e[9](t), l = !0;
    },
    p(n, c) {
      r && r.p && (!l || c & /*$$scope*/
      64) && ve(
        r,
        o,
        n,
        /*$$scope*/
        n[6],
        l ? be(
          o,
          /*$$scope*/
          n[6],
          c,
          null
        ) : we(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      l || (x(r, n), l = !0);
    },
    o(n) {
      T(r, n), l = !1;
    },
    d(n) {
      n && E(t), r && r.d(n), e[9](null);
    }
  };
}
function Oe(e) {
  let t, l, o, r, n = (
    /*$$slots*/
    e[4].default && G(e)
  );
  return {
    c() {
      t = K("react-portal-target"), l = Re(), n && n.c(), o = W(), this.h();
    },
    l(c) {
      t = Y(c, "REACT-PORTAL-TARGET", {
        class: !0
      }), J(t).forEach(E), l = he(c), n && n.l(c), o = W(), this.h();
    },
    h() {
      Q(t, "class", "svelte-1rt0kpf");
    },
    m(c, s) {
      v(c, t, s), e[8](t), v(c, l, s), n && n.m(c, s), v(c, o, s), r = !0;
    },
    p(c, [s]) {
      /*$$slots*/
      c[4].default ? n ? (n.p(c, s), s & /*$$slots*/
      16 && x(n, 1)) : (n = G(c), n.c(), x(n, 1), n.m(o.parentNode, o)) : n && (ye(), T(n, 1, 1, () => {
        n = null;
      }), me());
    },
    i(c) {
      r || (x(n), r = !0);
    },
    o(c) {
      T(n), r = !1;
    },
    d(c) {
      c && (E(t), E(l), E(o)), e[8](null), n && n.d(c);
    }
  };
}
function U(e) {
  const {
    svelteInit: t,
    ...l
  } = e;
  return l;
}
function je(e, t, l) {
  let o, r, {
    $$slots: n = {},
    $$scope: c
  } = t;
  const s = pe(n);
  let {
    svelteInit: a
  } = t;
  const m = R(U(t)), u = R();
  M(e, u, (d) => l(0, o = d));
  const h = R();
  M(e, h, (d) => l(1, r = d));
  const i = [], f = Ce("$$ms-gr-react-wrapper"), {
    slotKey: _,
    slotIndex: p,
    subSlotIndex: S
  } = oe() || {}, k = a({
    parent: f,
    props: m,
    target: u,
    slot: h,
    slotKey: _,
    slotIndex: p,
    subSlotIndex: S,
    onDestroy(d) {
      i.push(d);
    }
  });
  ke("$$ms-gr-react-wrapper", k), xe(() => {
    m.set(U(t));
  }), Se(() => {
    i.forEach((d) => d());
  });
  function O(d) {
    D[d ? "unshift" : "push"](() => {
      o = d, u.set(o);
    });
  }
  function j(d) {
    D[d ? "unshift" : "push"](() => {
      r = d, h.set(r);
    });
  }
  return e.$$set = (d) => {
    l(17, t = A(A({}, t), z(d))), "svelteInit" in d && l(5, a = d.svelteInit), "$$scope" in d && l(6, c = d.$$scope);
  }, t = z(t), [o, r, u, h, s, a, c, n, O, j];
}
class Fe extends _e {
  constructor(t) {
    super(), Ee(this, t, je, Oe, Ie, {
      svelteInit: 5
    });
  }
}
const H = window.ms_globals.rerender, F = window.ms_globals.tree;
function Pe(e) {
  function t(l) {
    const o = R(), r = new Fe({
      ...l,
      props: {
        svelteInit(n) {
          window.ms_globals.autokey += 1;
          const c = {
            key: window.ms_globals.autokey,
            svelteInstance: o,
            reactComponent: e,
            props: n.props,
            slot: n.slot,
            target: n.target,
            slotIndex: n.slotIndex,
            subSlotIndex: n.subSlotIndex,
            slotKey: n.slotKey,
            nodes: []
          }, s = n.parent ?? F;
          return s.nodes = [...s.nodes, c], H({
            createPortal: P,
            node: F
          }), n.onDestroy(() => {
            s.nodes = s.nodes.filter((a) => a.svelteInstance !== o), H({
              createPortal: P,
              node: F
            });
          }), c;
        },
        ...l.props
      }
    });
    return o.set(r), r;
  }
  return new Promise((l) => {
    window.ms_globals.initializePromise.then(() => {
      l(t);
    });
  });
}
const Te = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Le(e) {
  return e ? Object.keys(e).reduce((t, l) => {
    const o = e[l];
    return typeof o == "number" && !Te.includes(l) ? t[l] = o + "px" : t[l] = o, t;
  }, {}) : {};
}
function L(e) {
  const t = [], l = e.cloneNode(!1);
  if (e._reactElement)
    return t.push(P(y.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: y.Children.toArray(e._reactElement.props.children).map((r) => {
        if (y.isValidElement(r) && r.props.__slot__) {
          const {
            portals: n,
            clonedElement: c
          } = L(r.props.el);
          return y.cloneElement(r, {
            ...r.props,
            el: c,
            children: [...y.Children.toArray(r.props.children), ...n]
          });
        }
        return null;
      })
    }), l)), {
      clonedElement: l,
      portals: t
    };
  Object.keys(e.getEventListeners()).forEach((r) => {
    e.getEventListeners(r).forEach(({
      listener: c,
      type: s,
      useCapture: a
    }) => {
      l.addEventListener(s, c, a);
    });
  });
  const o = Array.from(e.childNodes);
  for (let r = 0; r < o.length; r++) {
    const n = o[r];
    if (n.nodeType === 1) {
      const {
        clonedElement: c,
        portals: s
      } = L(n);
      t.push(...s), l.appendChild(c);
    } else n.nodeType === 3 && l.appendChild(n.cloneNode());
  }
  return {
    clonedElement: l,
    portals: t
  };
}
function Ne(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const w = te(({
  slot: e,
  clone: t,
  className: l,
  style: o
}, r) => {
  const n = ne(), [c, s] = re([]);
  return le(() => {
    var h;
    if (!n.current || !e)
      return;
    let a = e;
    function m() {
      let i = a;
      if (a.tagName.toLowerCase() === "svelte-slot" && a.children.length === 1 && a.children[0] && (i = a.children[0], i.tagName.toLowerCase() === "react-portal-target" && i.children[0] && (i = i.children[0])), Ne(r, i), l && i.classList.add(...l.split(" ")), o) {
        const f = Le(o);
        Object.keys(f).forEach((_) => {
          i.style[_] = f[_];
        });
      }
    }
    let u = null;
    if (t && window.MutationObserver) {
      let i = function() {
        var p;
        const {
          portals: f,
          clonedElement: _
        } = L(e);
        a = _, s(f), a.style.display = "contents", m(), (p = n.current) == null || p.appendChild(a);
      };
      i(), u = new window.MutationObserver(() => {
        var f, _;
        (f = n.current) != null && f.contains(a) && ((_ = n.current) == null || _.removeChild(a)), i();
      }), u.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      a.style.display = "contents", m(), (h = n.current) == null || h.appendChild(a);
    return () => {
      var i, f;
      a.style.display = "", (i = n.current) != null && i.contains(a) && ((f = n.current) == null || f.removeChild(a)), u == null || u.disconnect();
    };
  }, [e, t, l, o, r]), y.createElement("react-child", {
    ref: n,
    style: {
      display: "contents"
    }
  }, ...c);
});
function Ae(e) {
  try {
    return typeof e == "string" ? new Function(`return (...args) => (${e})(...args)`)() : void 0;
  } catch {
    return;
  }
}
function b(e) {
  return q(() => Ae(e), [e]);
}
function X(e, t) {
  return e.filter(Boolean).map((l) => {
    if (typeof l != "object")
      return t != null && t.fallback ? t.fallback(l) : l;
    const o = {
      ...l.props
    };
    let r = o;
    Object.keys(l.slots).forEach((c) => {
      if (!l.slots[c] || !(l.slots[c] instanceof Element) && !l.slots[c].el)
        return;
      const s = c.split(".");
      s.forEach((i, f) => {
        r[i] || (r[i] = {}), f !== s.length - 1 && (r = o[i]);
      });
      const a = l.slots[c];
      let m, u, h = !1;
      a instanceof Element ? m = a : (m = a.el, u = a.callback, h = a.clone || !1), r[s[s.length - 1]] = m ? u ? (...i) => (u(s[s.length - 1], i), /* @__PURE__ */ g.jsx(w, {
        slot: m,
        clone: h || (t == null ? void 0 : t.clone)
      })) : /* @__PURE__ */ g.jsx(w, {
        slot: m,
        clone: h || (t == null ? void 0 : t.clone)
      }) : r[s[s.length - 1]], r = o;
    });
    const n = (t == null ? void 0 : t.children) || "children";
    return l[n] && (o[n] = X(l[n], t)), o;
  });
}
function De(e, t) {
  return e ? /* @__PURE__ */ g.jsx(w, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function I({
  key: e,
  setSlotParams: t,
  slots: l
}, o) {
  return (...r) => (t(e, r), De(l[e], {
    clone: !0,
    ...o
  }));
}
const We = Pe(({
  slots: e,
  children: t,
  onValueChange: l,
  filterOption: o,
  onChange: r,
  options: n,
  optionItems: c,
  getPopupContainer: s,
  dropdownRender: a,
  optionRender: m,
  tagRender: u,
  labelRender: h,
  filterSort: i,
  elRef: f,
  setSlotParams: _,
  ...p
}) => {
  const S = b(s), k = b(o), O = b(a), j = b(i), d = b(m), Z = b(u), $ = b(h);
  return /* @__PURE__ */ g.jsxs(g.Fragment, {
    children: [/* @__PURE__ */ g.jsx("div", {
      style: {
        display: "none"
      },
      children: t
    }), /* @__PURE__ */ g.jsx(ce, {
      ...p,
      ref: f,
      options: q(() => n || X(c, {
        children: "options",
        clone: !0
      }), [c, n]),
      onChange: (N, ...ee) => {
        r == null || r(N, ...ee), l(N);
      },
      allowClear: e["allowClear.clearIcon"] ? {
        clearIcon: /* @__PURE__ */ g.jsx(w, {
          slot: e["allowClear.clearIcon"]
        })
      } : p.allowClear,
      removeIcon: e.removeIcon ? /* @__PURE__ */ g.jsx(w, {
        slot: e.removeIcon
      }) : p.removeIcon,
      suffixIcon: e.suffixIcon ? /* @__PURE__ */ g.jsx(w, {
        slot: e.suffixIcon
      }) : p.suffixIcon,
      notFoundContent: e.notFoundContent ? /* @__PURE__ */ g.jsx(w, {
        slot: e.notFoundContent
      }) : p.notFoundContent,
      menuItemSelectedIcon: e.menuItemSelectedIcon ? /* @__PURE__ */ g.jsx(w, {
        slot: e.menuItemSelectedIcon
      }) : p.menuItemSelectedIcon,
      filterOption: k || o,
      maxTagPlaceholder: e.maxTagPlaceholder ? I({
        slots: e,
        setSlotParams: _,
        key: "maxTagPlaceholder"
      }) : p.maxTagPlaceholder,
      getPopupContainer: S,
      dropdownRender: e.dropdownRender ? I({
        slots: e,
        setSlotParams: _,
        key: "dropdownRender"
      }) : O,
      optionRender: e.optionRender ? I({
        slots: e,
        setSlotParams: _,
        key: "optionRender"
      }) : d,
      tagRender: e.tagRender ? I({
        slots: e,
        setSlotParams: _,
        key: "tagRender"
      }) : Z,
      labelRender: e.labelRender ? I({
        slots: e,
        setSlotParams: _,
        key: "labelRender"
      }) : $,
      filterSort: j
    })]
  });
});
export {
  We as Select,
  We as default
};
