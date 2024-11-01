import { g as $, w as E } from "./Index-D31EOlWv.js";
const h = window.ms_globals.React, Y = window.ms_globals.React.forwardRef, K = window.ms_globals.React.useRef, Q = window.ms_globals.React.useState, X = window.ms_globals.React.useEffect, Z = window.ms_globals.React.useMemo, R = window.ms_globals.ReactDOM.createPortal, ee = window.ms_globals.antd.Menu;
var F = {
  exports: {}
}, I = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var te = h, ne = Symbol.for("react.element"), re = Symbol.for("react.fragment"), le = Object.prototype.hasOwnProperty, oe = te.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, se = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function U(n, t, r) {
  var s, l = {}, e = null, o = null;
  r !== void 0 && (e = "" + r), t.key !== void 0 && (e = "" + t.key), t.ref !== void 0 && (o = t.ref);
  for (s in t) le.call(t, s) && !se.hasOwnProperty(s) && (l[s] = t[s]);
  if (n && n.defaultProps) for (s in t = n.defaultProps, t) l[s] === void 0 && (l[s] = t[s]);
  return {
    $$typeof: ne,
    type: n,
    key: e,
    ref: o,
    props: l,
    _owner: oe.current
  };
}
I.Fragment = re;
I.jsx = U;
I.jsxs = U;
F.exports = I;
var g = F.exports;
const {
  SvelteComponent: ce,
  assign: k,
  binding_callbacks: j,
  check_outros: ie,
  children: W,
  claim_element: z,
  claim_space: ae,
  component_subscribe: P,
  compute_slots: de,
  create_slot: ue,
  detach: w,
  element: G,
  empty: L,
  exclude_internal_props: T,
  get_all_dirty_from_scope: fe,
  get_slot_changes: _e,
  group_outros: me,
  init: pe,
  insert_hydration: v,
  safe_not_equal: he,
  set_custom_element_data: D,
  space: ge,
  transition_in: y,
  transition_out: S,
  update_slot_base: we
} = window.__gradio__svelte__internal, {
  beforeUpdate: be,
  getContext: Ee,
  onDestroy: ve,
  setContext: ye
} = window.__gradio__svelte__internal;
function N(n) {
  let t, r;
  const s = (
    /*#slots*/
    n[7].default
  ), l = ue(
    s,
    n,
    /*$$scope*/
    n[6],
    null
  );
  return {
    c() {
      t = G("svelte-slot"), l && l.c(), this.h();
    },
    l(e) {
      t = z(e, "SVELTE-SLOT", {
        class: !0
      });
      var o = W(t);
      l && l.l(o), o.forEach(w), this.h();
    },
    h() {
      D(t, "class", "svelte-1rt0kpf");
    },
    m(e, o) {
      v(e, t, o), l && l.m(t, null), n[9](t), r = !0;
    },
    p(e, o) {
      l && l.p && (!r || o & /*$$scope*/
      64) && we(
        l,
        s,
        e,
        /*$$scope*/
        e[6],
        r ? _e(
          s,
          /*$$scope*/
          e[6],
          o,
          null
        ) : fe(
          /*$$scope*/
          e[6]
        ),
        null
      );
    },
    i(e) {
      r || (y(l, e), r = !0);
    },
    o(e) {
      S(l, e), r = !1;
    },
    d(e) {
      e && w(t), l && l.d(e), n[9](null);
    }
  };
}
function xe(n) {
  let t, r, s, l, e = (
    /*$$slots*/
    n[4].default && N(n)
  );
  return {
    c() {
      t = G("react-portal-target"), r = ge(), e && e.c(), s = L(), this.h();
    },
    l(o) {
      t = z(o, "REACT-PORTAL-TARGET", {
        class: !0
      }), W(t).forEach(w), r = ae(o), e && e.l(o), s = L(), this.h();
    },
    h() {
      D(t, "class", "svelte-1rt0kpf");
    },
    m(o, i) {
      v(o, t, i), n[8](t), v(o, r, i), e && e.m(o, i), v(o, s, i), l = !0;
    },
    p(o, [i]) {
      /*$$slots*/
      o[4].default ? e ? (e.p(o, i), i & /*$$slots*/
      16 && y(e, 1)) : (e = N(o), e.c(), y(e, 1), e.m(s.parentNode, s)) : e && (me(), S(e, 1, 1, () => {
        e = null;
      }), ie());
    },
    i(o) {
      l || (y(e), l = !0);
    },
    o(o) {
      S(e), l = !1;
    },
    d(o) {
      o && (w(t), w(r), w(s)), n[8](null), e && e.d(o);
    }
  };
}
function A(n) {
  const {
    svelteInit: t,
    ...r
  } = n;
  return r;
}
function Ie(n, t, r) {
  let s, l, {
    $$slots: e = {},
    $$scope: o
  } = t;
  const i = de(e);
  let {
    svelteInit: c
  } = t;
  const u = E(A(t)), f = E();
  P(n, f, (d) => r(0, s = d));
  const m = E();
  P(n, m, (d) => r(1, l = d));
  const a = [], _ = Ee("$$ms-gr-react-wrapper"), {
    slotKey: p,
    slotIndex: b,
    subSlotIndex: q
  } = $() || {}, B = c({
    parent: _,
    props: u,
    target: f,
    slot: m,
    slotKey: p,
    slotIndex: b,
    subSlotIndex: q,
    onDestroy(d) {
      a.push(d);
    }
  });
  ye("$$ms-gr-react-wrapper", B), be(() => {
    u.set(A(t));
  }), ve(() => {
    a.forEach((d) => d());
  });
  function V(d) {
    j[d ? "unshift" : "push"](() => {
      s = d, f.set(s);
    });
  }
  function J(d) {
    j[d ? "unshift" : "push"](() => {
      l = d, m.set(l);
    });
  }
  return n.$$set = (d) => {
    r(17, t = k(k({}, t), T(d))), "svelteInit" in d && r(5, c = d.svelteInit), "$$scope" in d && r(6, o = d.$$scope);
  }, t = T(t), [s, l, f, m, i, c, o, e, V, J];
}
class Ce extends ce {
  constructor(t) {
    super(), pe(this, t, Ie, xe, he, {
      svelteInit: 5
    });
  }
}
const M = window.ms_globals.rerender, C = window.ms_globals.tree;
function Re(n) {
  function t(r) {
    const s = E(), l = new Ce({
      ...r,
      props: {
        svelteInit(e) {
          window.ms_globals.autokey += 1;
          const o = {
            key: window.ms_globals.autokey,
            svelteInstance: s,
            reactComponent: n,
            props: e.props,
            slot: e.slot,
            target: e.target,
            slotIndex: e.slotIndex,
            subSlotIndex: e.subSlotIndex,
            slotKey: e.slotKey,
            nodes: []
          }, i = e.parent ?? C;
          return i.nodes = [...i.nodes, o], M({
            createPortal: R,
            node: C
          }), e.onDestroy(() => {
            i.nodes = i.nodes.filter((c) => c.svelteInstance !== s), M({
              createPortal: R,
              node: C
            });
          }), o;
        },
        ...r.props
      }
    });
    return s.set(l), l;
  }
  return new Promise((r) => {
    window.ms_globals.initializePromise.then(() => {
      r(t);
    });
  });
}
const Se = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Oe(n) {
  return n ? Object.keys(n).reduce((t, r) => {
    const s = n[r];
    return typeof s == "number" && !Se.includes(r) ? t[r] = s + "px" : t[r] = s, t;
  }, {}) : {};
}
function O(n) {
  const t = [], r = n.cloneNode(!1);
  if (n._reactElement)
    return t.push(R(h.cloneElement(n._reactElement, {
      ...n._reactElement.props,
      children: h.Children.toArray(n._reactElement.props.children).map((l) => {
        if (h.isValidElement(l) && l.props.__slot__) {
          const {
            portals: e,
            clonedElement: o
          } = O(l.props.el);
          return h.cloneElement(l, {
            ...l.props,
            el: o,
            children: [...h.Children.toArray(l.props.children), ...e]
          });
        }
        return null;
      })
    }), r)), {
      clonedElement: r,
      portals: t
    };
  Object.keys(n.getEventListeners()).forEach((l) => {
    n.getEventListeners(l).forEach(({
      listener: o,
      type: i,
      useCapture: c
    }) => {
      r.addEventListener(i, o, c);
    });
  });
  const s = Array.from(n.childNodes);
  for (let l = 0; l < s.length; l++) {
    const e = s[l];
    if (e.nodeType === 1) {
      const {
        clonedElement: o,
        portals: i
      } = O(e);
      t.push(...i), r.appendChild(o);
    } else e.nodeType === 3 && r.appendChild(e.cloneNode());
  }
  return {
    clonedElement: r,
    portals: t
  };
}
function ke(n, t) {
  n && (typeof n == "function" ? n(t) : n.current = t);
}
const x = Y(({
  slot: n,
  clone: t,
  className: r,
  style: s
}, l) => {
  const e = K(), [o, i] = Q([]);
  return X(() => {
    var m;
    if (!e.current || !n)
      return;
    let c = n;
    function u() {
      let a = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (a = c.children[0], a.tagName.toLowerCase() === "react-portal-target" && a.children[0] && (a = a.children[0])), ke(l, a), r && a.classList.add(...r.split(" ")), s) {
        const _ = Oe(s);
        Object.keys(_).forEach((p) => {
          a.style[p] = _[p];
        });
      }
    }
    let f = null;
    if (t && window.MutationObserver) {
      let a = function() {
        var b;
        const {
          portals: _,
          clonedElement: p
        } = O(n);
        c = p, i(_), c.style.display = "contents", u(), (b = e.current) == null || b.appendChild(c);
      };
      a(), f = new window.MutationObserver(() => {
        var _, p;
        (_ = e.current) != null && _.contains(c) && ((p = e.current) == null || p.removeChild(c)), a();
      }), f.observe(n, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", u(), (m = e.current) == null || m.appendChild(c);
    return () => {
      var a, _;
      c.style.display = "", (a = e.current) != null && a.contains(c) && ((_ = e.current) == null || _.removeChild(c)), f == null || f.disconnect();
    };
  }, [n, t, r, s, l]), h.createElement("react-child", {
    ref: e,
    style: {
      display: "contents"
    }
  }, ...o);
});
function je(n) {
  return Object.keys(n).reduce((t, r) => (n[r] !== void 0 && (t[r] = n[r]), t), {});
}
function H(n, t) {
  return n.filter(Boolean).map((r) => {
    if (typeof r != "object")
      return r;
    const s = {
      ...r.props
    };
    let l = s;
    Object.keys(r.slots).forEach((o) => {
      if (!r.slots[o] || !(r.slots[o] instanceof Element) && !r.slots[o].el)
        return;
      const i = o.split(".");
      i.forEach((a, _) => {
        l[a] || (l[a] = {}), _ !== i.length - 1 && (l = s[a]);
      });
      const c = r.slots[o];
      let u, f, m = !1;
      c instanceof Element ? u = c : (u = c.el, f = c.callback, m = c.clone || !1), l[i[i.length - 1]] = u ? f ? (...a) => (f(i[i.length - 1], a), /* @__PURE__ */ g.jsx(x, {
        slot: u,
        clone: m || (t == null ? void 0 : t.clone)
      })) : /* @__PURE__ */ g.jsx(x, {
        slot: u,
        clone: m || (t == null ? void 0 : t.clone)
      }) : l[i[i.length - 1]], l = s;
    });
    const e = "children";
    return r[e] && (s[e] = H(r[e], t)), s;
  });
}
function Pe(n, t) {
  return n ? /* @__PURE__ */ g.jsx(x, {
    slot: n,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function Le({
  key: n,
  setSlotParams: t,
  slots: r
}, s) {
  return (...l) => (t(n, l), Pe(r[n], {
    clone: !0,
    ...s
  }));
}
const Ne = Re(({
  slots: n,
  items: t,
  slotItems: r,
  children: s,
  onOpenChange: l,
  onSelect: e,
  onDeselect: o,
  setSlotParams: i,
  ...c
}) => /* @__PURE__ */ g.jsxs(g.Fragment, {
  children: [s, /* @__PURE__ */ g.jsx(ee, {
    ...je(c),
    onOpenChange: (u) => {
      l == null || l(u);
    },
    onSelect: (u) => {
      e == null || e(u);
    },
    onDeselect: (u) => {
      o == null || o(u);
    },
    items: Z(() => t || H(r), [t, r]),
    expandIcon: n.expandIcon ? Le({
      key: "expandIcon",
      slots: n,
      setSlotParams: i
    }, {
      clone: !0
    }) : c.expandIcon,
    overflowedIndicator: n.overflowedIndicator ? /* @__PURE__ */ g.jsx(x, {
      slot: n.overflowedIndicator
    }) : c.overflowedIndicator
  })]
}));
export {
  Ne as Menu,
  Ne as default
};
