import { g as ye, w as O } from "./Index-DFlij4C_.js";
const w = window.ms_globals.React, he = window.ms_globals.React.forwardRef, ve = window.ms_globals.React.useRef, be = window.ms_globals.React.useState, ge = window.ms_globals.React.useEffect, v = window.ms_globals.React.useMemo, M = window.ms_globals.ReactDOM.createPortal, we = window.ms_globals.antd.DatePicker, z = window.ms_globals.dayjs;
var X = {
  exports: {}
}, D = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var xe = w, Ee = Symbol.for("react.element"), Ie = Symbol.for("react.fragment"), Re = Object.prototype.hasOwnProperty, Ce = xe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, je = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function Z(e, t, o) {
  var l, r = {}, n = null, s = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (s = t.ref);
  for (l in t) Re.call(t, l) && !je.hasOwnProperty(l) && (r[l] = t[l]);
  if (e && e.defaultProps) for (l in t = e.defaultProps, t) r[l] === void 0 && (r[l] = t[l]);
  return {
    $$typeof: Ee,
    type: e,
    key: n,
    ref: s,
    props: r,
    _owner: Ce.current
  };
}
D.Fragment = Ie;
D.jsx = Z;
D.jsxs = Z;
X.exports = D;
var m = X.exports;
const {
  SvelteComponent: ke,
  assign: G,
  binding_callbacks: U,
  check_outros: Oe,
  children: $,
  claim_element: ee,
  claim_space: Se,
  component_subscribe: H,
  compute_slots: Pe,
  create_slot: De,
  detach: I,
  element: te,
  empty: q,
  exclude_internal_props: B,
  get_all_dirty_from_scope: Fe,
  get_slot_changes: Ne,
  group_outros: Ae,
  init: Le,
  insert_hydration: S,
  safe_not_equal: Te,
  set_custom_element_data: ne,
  space: Me,
  transition_in: P,
  transition_out: V,
  update_slot_base: Ve
} = window.__gradio__svelte__internal, {
  beforeUpdate: We,
  getContext: ze,
  onDestroy: Ge,
  setContext: Ue
} = window.__gradio__svelte__internal;
function J(e) {
  let t, o;
  const l = (
    /*#slots*/
    e[7].default
  ), r = De(
    l,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = te("svelte-slot"), r && r.c(), this.h();
    },
    l(n) {
      t = ee(n, "SVELTE-SLOT", {
        class: !0
      });
      var s = $(t);
      r && r.l(s), s.forEach(I), this.h();
    },
    h() {
      ne(t, "class", "svelte-1rt0kpf");
    },
    m(n, s) {
      S(n, t, s), r && r.m(t, null), e[9](t), o = !0;
    },
    p(n, s) {
      r && r.p && (!o || s & /*$$scope*/
      64) && Ve(
        r,
        l,
        n,
        /*$$scope*/
        n[6],
        o ? Ne(
          l,
          /*$$scope*/
          n[6],
          s,
          null
        ) : Fe(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (P(r, n), o = !0);
    },
    o(n) {
      V(r, n), o = !1;
    },
    d(n) {
      n && I(t), r && r.d(n), e[9](null);
    }
  };
}
function He(e) {
  let t, o, l, r, n = (
    /*$$slots*/
    e[4].default && J(e)
  );
  return {
    c() {
      t = te("react-portal-target"), o = Me(), n && n.c(), l = q(), this.h();
    },
    l(s) {
      t = ee(s, "REACT-PORTAL-TARGET", {
        class: !0
      }), $(t).forEach(I), o = Se(s), n && n.l(s), l = q(), this.h();
    },
    h() {
      ne(t, "class", "svelte-1rt0kpf");
    },
    m(s, c) {
      S(s, t, c), e[8](t), S(s, o, c), n && n.m(s, c), S(s, l, c), r = !0;
    },
    p(s, [c]) {
      /*$$slots*/
      s[4].default ? n ? (n.p(s, c), c & /*$$slots*/
      16 && P(n, 1)) : (n = J(s), n.c(), P(n, 1), n.m(l.parentNode, l)) : n && (Ae(), V(n, 1, 1, () => {
        n = null;
      }), Oe());
    },
    i(s) {
      r || (P(n), r = !0);
    },
    o(s) {
      V(n), r = !1;
    },
    d(s) {
      s && (I(t), I(o), I(l)), e[8](null), n && n.d(s);
    }
  };
}
function Y(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function qe(e, t, o) {
  let l, r, {
    $$slots: n = {},
    $$scope: s
  } = t;
  const c = Pe(n);
  let {
    svelteInit: i
  } = t;
  const p = O(Y(t)), d = O();
  H(e, d, (u) => o(0, l = u));
  const _ = O();
  H(e, _, (u) => o(1, r = u));
  const a = [], f = ze("$$ms-gr-react-wrapper"), {
    slotKey: h,
    slotIndex: x,
    subSlotIndex: F
  } = ye() || {}, R = i({
    parent: f,
    props: p,
    target: d,
    slot: _,
    slotKey: h,
    slotIndex: x,
    subSlotIndex: F,
    onDestroy(u) {
      a.push(u);
    }
  });
  Ue("$$ms-gr-react-wrapper", R), We(() => {
    p.set(Y(t));
  }), Ge(() => {
    a.forEach((u) => u());
  });
  function N(u) {
    U[u ? "unshift" : "push"](() => {
      l = u, d.set(l);
    });
  }
  function C(u) {
    U[u ? "unshift" : "push"](() => {
      r = u, _.set(r);
    });
  }
  return e.$$set = (u) => {
    o(17, t = G(G({}, t), B(u))), "svelteInit" in u && o(5, i = u.svelteInit), "$$scope" in u && o(6, s = u.$$scope);
  }, t = B(t), [l, r, d, _, c, i, s, n, N, C];
}
class Be extends ke {
  constructor(t) {
    super(), Le(this, t, qe, He, Te, {
      svelteInit: 5
    });
  }
}
const K = window.ms_globals.rerender, L = window.ms_globals.tree;
function Je(e) {
  function t(o) {
    const l = O(), r = new Be({
      ...o,
      props: {
        svelteInit(n) {
          window.ms_globals.autokey += 1;
          const s = {
            key: window.ms_globals.autokey,
            svelteInstance: l,
            reactComponent: e,
            props: n.props,
            slot: n.slot,
            target: n.target,
            slotIndex: n.slotIndex,
            subSlotIndex: n.subSlotIndex,
            slotKey: n.slotKey,
            nodes: []
          }, c = n.parent ?? L;
          return c.nodes = [...c.nodes, s], K({
            createPortal: M,
            node: L
          }), n.onDestroy(() => {
            c.nodes = c.nodes.filter((i) => i.svelteInstance !== l), K({
              createPortal: M,
              node: L
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
const Ye = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Ke(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const l = e[o];
    return typeof l == "number" && !Ye.includes(o) ? t[o] = l + "px" : t[o] = l, t;
  }, {}) : {};
}
function W(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement)
    return t.push(M(w.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: w.Children.toArray(e._reactElement.props.children).map((r) => {
        if (w.isValidElement(r) && r.props.__slot__) {
          const {
            portals: n,
            clonedElement: s
          } = W(r.props.el);
          return w.cloneElement(r, {
            ...r.props,
            el: s,
            children: [...w.Children.toArray(r.props.children), ...n]
          });
        }
        return null;
      })
    }), o)), {
      clonedElement: o,
      portals: t
    };
  Object.keys(e.getEventListeners()).forEach((r) => {
    e.getEventListeners(r).forEach(({
      listener: s,
      type: c,
      useCapture: i
    }) => {
      o.addEventListener(c, s, i);
    });
  });
  const l = Array.from(e.childNodes);
  for (let r = 0; r < l.length; r++) {
    const n = l[r];
    if (n.nodeType === 1) {
      const {
        clonedElement: s,
        portals: c
      } = W(n);
      t.push(...c), o.appendChild(s);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function Qe(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const g = he(({
  slot: e,
  clone: t,
  className: o,
  style: l
}, r) => {
  const n = ve(), [s, c] = be([]);
  return ge(() => {
    var _;
    if (!n.current || !e)
      return;
    let i = e;
    function p() {
      let a = i;
      if (i.tagName.toLowerCase() === "svelte-slot" && i.children.length === 1 && i.children[0] && (a = i.children[0], a.tagName.toLowerCase() === "react-portal-target" && a.children[0] && (a = a.children[0])), Qe(r, a), o && a.classList.add(...o.split(" ")), l) {
        const f = Ke(l);
        Object.keys(f).forEach((h) => {
          a.style[h] = f[h];
        });
      }
    }
    let d = null;
    if (t && window.MutationObserver) {
      let a = function() {
        var x;
        const {
          portals: f,
          clonedElement: h
        } = W(e);
        i = h, c(f), i.style.display = "contents", p(), (x = n.current) == null || x.appendChild(i);
      };
      a(), d = new window.MutationObserver(() => {
        var f, h;
        (f = n.current) != null && f.contains(i) && ((h = n.current) == null || h.removeChild(i)), a();
      }), d.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      i.style.display = "contents", p(), (_ = n.current) == null || _.appendChild(i);
    return () => {
      var a, f;
      i.style.display = "", (a = n.current) != null && a.contains(i) && ((f = n.current) == null || f.removeChild(i)), d == null || d.disconnect();
    };
  }, [e, t, o, l, r]), w.createElement("react-child", {
    ref: n,
    style: {
      display: "contents"
    }
  }, ...s);
});
function Xe(e) {
  try {
    return typeof e == "string" ? new Function(`return (...args) => (${e})(...args)`)() : void 0;
  } catch {
    return;
  }
}
function j(e) {
  return v(() => Xe(e), [e]);
}
function re(e, t) {
  return e.filter(Boolean).map((o) => {
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
      let p, d, _ = !1;
      i instanceof Element ? p = i : (p = i.el, d = i.callback, _ = i.clone || !1), r[c[c.length - 1]] = p ? d ? (...a) => (d(c[c.length - 1], a), /* @__PURE__ */ m.jsx(g, {
        slot: p,
        clone: _ || (t == null ? void 0 : t.clone)
      })) : /* @__PURE__ */ m.jsx(g, {
        slot: p,
        clone: _ || (t == null ? void 0 : t.clone)
      }) : r[c[c.length - 1]], r = l;
    });
    const n = "children";
    return o[n] && (l[n] = re(o[n], t)), l;
  });
}
function Ze(e, t) {
  return e ? /* @__PURE__ */ m.jsx(g, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function T({
  key: e,
  setSlotParams: t,
  slots: o
}, l) {
  return (...r) => (t(e, r), Ze(o[e], {
    clone: !0,
    ...l
  }));
}
function b(e) {
  return Array.isArray(e) ? e.map((t) => b(t)) : z(typeof e == "number" ? e * 1e3 : e);
}
function Q(e) {
  return Array.isArray(e) ? e.map((t) => t ? t.valueOf() / 1e3 : null) : typeof e == "object" && e !== null ? e.valueOf() / 1e3 : e;
}
const et = Je(({
  slots: e,
  disabledDate: t,
  disabledTime: o,
  value: l,
  defaultValue: r,
  defaultPickerValue: n,
  pickerValue: s,
  showTime: c,
  presets: i,
  presetItems: p,
  onChange: d,
  minDate: _,
  maxDate: a,
  cellRender: f,
  panelRender: h,
  getPopupContainer: x,
  onValueChange: F,
  onPanelChange: R,
  children: N,
  setSlotParams: C,
  elRef: u,
  ...y
}) => {
  const oe = j(t), le = j(o), se = j(x), ce = j(f), ie = j(h), ae = v(() => typeof c == "object" ? {
    ...c,
    defaultValue: c.defaultValue ? b(c.defaultValue) : void 0
  } : c, [c]), ue = v(() => l ? b(l) : void 0, [l]), de = v(() => r ? b(r) : void 0, [r]), fe = v(() => n ? b(n) : void 0, [n]), _e = v(() => s ? b(s) : void 0, [s]), pe = v(() => _ ? b(_) : void 0, [_]), me = v(() => a ? b(a) : void 0, [a]);
  return /* @__PURE__ */ m.jsxs(m.Fragment, {
    children: [/* @__PURE__ */ m.jsx("div", {
      style: {
        display: "none"
      },
      children: N
    }), /* @__PURE__ */ m.jsx(we, {
      ...y,
      ref: u,
      value: ue,
      defaultValue: de,
      defaultPickerValue: fe,
      pickerValue: _e,
      minDate: pe,
      maxDate: me,
      showTime: ae,
      disabledDate: oe,
      disabledTime: le,
      getPopupContainer: se,
      cellRender: e.cellRender ? T({
        slots: e,
        setSlotParams: C,
        key: "cellRender"
      }) : ce,
      panelRender: e.panelRender ? T({
        slots: e,
        setSlotParams: C,
        key: "panelRender"
      }) : ie,
      presets: v(() => (i || re(p)).map((E) => ({
        ...E,
        value: b(E.value)
      })), [i, p]),
      onPanelChange: (E, ...A) => {
        const k = Q(E);
        R == null || R(k, ...A);
      },
      onChange: (E, ...A) => {
        const k = Q(E);
        d == null || d(k, ...A), F(k);
      },
      renderExtraFooter: e.renderExtraFooter ? T({
        slots: e,
        setSlotParams: C,
        key: "renderExtraFooter"
      }) : y.renderExtraFooter,
      prevIcon: e.prevIcon ? /* @__PURE__ */ m.jsx(g, {
        slot: e.prevIcon
      }) : y.prevIcon,
      nextIcon: e.nextIcon ? /* @__PURE__ */ m.jsx(g, {
        slot: e.nextIcon
      }) : y.nextIcon,
      suffixIcon: e.suffixIcon ? /* @__PURE__ */ m.jsx(g, {
        slot: e.suffixIcon
      }) : y.suffixIcon,
      superNextIcon: e.superNextIcon ? /* @__PURE__ */ m.jsx(g, {
        slot: e.superNextIcon
      }) : y.superNextIcon,
      superPrevIcon: e.superPrevIcon ? /* @__PURE__ */ m.jsx(g, {
        slot: e.superPrevIcon
      }) : y.superPrevIcon,
      allowClear: e["allowClear.clearIcon"] ? {
        clearIcon: /* @__PURE__ */ m.jsx(g, {
          slot: e["allowClear.clearIcon"]
        })
      } : y.allowClear
    })]
  });
});
export {
  et as DatePicker,
  et as default
};
