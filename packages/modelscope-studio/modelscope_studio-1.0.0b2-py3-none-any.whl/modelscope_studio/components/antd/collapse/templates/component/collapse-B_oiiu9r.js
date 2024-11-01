import { g as $, w as E } from "./Index-BjbbrsAi.js";
const h = window.ms_globals.React, D = window.ms_globals.React.useMemo, K = window.ms_globals.React.forwardRef, Q = window.ms_globals.React.useRef, X = window.ms_globals.React.useState, Z = window.ms_globals.React.useEffect, I = window.ms_globals.ReactDOM.createPortal, ee = window.ms_globals.antd.Collapse;
var M = {
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
var te = h, ne = Symbol.for("react.element"), re = Symbol.for("react.fragment"), le = Object.prototype.hasOwnProperty, oe = te.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, se = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function W(n, t, l) {
  var o, r = {}, e = null, s = null;
  l !== void 0 && (e = "" + l), t.key !== void 0 && (e = "" + t.key), t.ref !== void 0 && (s = t.ref);
  for (o in t) le.call(t, o) && !se.hasOwnProperty(o) && (r[o] = t[o]);
  if (n && n.defaultProps) for (o in t = n.defaultProps, t) r[o] === void 0 && (r[o] = t[o]);
  return {
    $$typeof: ne,
    type: n,
    key: e,
    ref: s,
    props: r,
    _owner: oe.current
  };
}
x.Fragment = re;
x.jsx = W;
x.jsxs = W;
M.exports = x;
var w = M.exports;
const {
  SvelteComponent: ce,
  assign: k,
  binding_callbacks: P,
  check_outros: ie,
  children: z,
  claim_element: G,
  claim_space: ae,
  component_subscribe: j,
  compute_slots: ue,
  create_slot: de,
  detach: g,
  element: U,
  empty: L,
  exclude_internal_props: T,
  get_all_dirty_from_scope: fe,
  get_slot_changes: _e,
  group_outros: pe,
  init: me,
  insert_hydration: y,
  safe_not_equal: he,
  set_custom_element_data: H,
  space: ge,
  transition_in: v,
  transition_out: R,
  update_slot_base: we
} = window.__gradio__svelte__internal, {
  beforeUpdate: be,
  getContext: Ee,
  onDestroy: ye,
  setContext: ve
} = window.__gradio__svelte__internal;
function N(n) {
  let t, l;
  const o = (
    /*#slots*/
    n[7].default
  ), r = de(
    o,
    n,
    /*$$scope*/
    n[6],
    null
  );
  return {
    c() {
      t = U("svelte-slot"), r && r.c(), this.h();
    },
    l(e) {
      t = G(e, "SVELTE-SLOT", {
        class: !0
      });
      var s = z(t);
      r && r.l(s), s.forEach(g), this.h();
    },
    h() {
      H(t, "class", "svelte-1rt0kpf");
    },
    m(e, s) {
      y(e, t, s), r && r.m(t, null), n[9](t), l = !0;
    },
    p(e, s) {
      r && r.p && (!l || s & /*$$scope*/
      64) && we(
        r,
        o,
        e,
        /*$$scope*/
        e[6],
        l ? _e(
          o,
          /*$$scope*/
          e[6],
          s,
          null
        ) : fe(
          /*$$scope*/
          e[6]
        ),
        null
      );
    },
    i(e) {
      l || (v(r, e), l = !0);
    },
    o(e) {
      R(r, e), l = !1;
    },
    d(e) {
      e && g(t), r && r.d(e), n[9](null);
    }
  };
}
function xe(n) {
  let t, l, o, r, e = (
    /*$$slots*/
    n[4].default && N(n)
  );
  return {
    c() {
      t = U("react-portal-target"), l = ge(), e && e.c(), o = L(), this.h();
    },
    l(s) {
      t = G(s, "REACT-PORTAL-TARGET", {
        class: !0
      }), z(t).forEach(g), l = ae(s), e && e.l(s), o = L(), this.h();
    },
    h() {
      H(t, "class", "svelte-1rt0kpf");
    },
    m(s, c) {
      y(s, t, c), n[8](t), y(s, l, c), e && e.m(s, c), y(s, o, c), r = !0;
    },
    p(s, [c]) {
      /*$$slots*/
      s[4].default ? e ? (e.p(s, c), c & /*$$slots*/
      16 && v(e, 1)) : (e = N(s), e.c(), v(e, 1), e.m(o.parentNode, o)) : e && (pe(), R(e, 1, 1, () => {
        e = null;
      }), ie());
    },
    i(s) {
      r || (v(e), r = !0);
    },
    o(s) {
      R(e), r = !1;
    },
    d(s) {
      s && (g(t), g(l), g(o)), n[8](null), e && e.d(s);
    }
  };
}
function A(n) {
  const {
    svelteInit: t,
    ...l
  } = n;
  return l;
}
function Ce(n, t, l) {
  let o, r, {
    $$slots: e = {},
    $$scope: s
  } = t;
  const c = ue(e);
  let {
    svelteInit: i
  } = t;
  const _ = E(A(t)), d = E();
  j(n, d, (u) => l(0, o = u));
  const p = E();
  j(n, p, (u) => l(1, r = u));
  const a = [], f = Ee("$$ms-gr-react-wrapper"), {
    slotKey: m,
    slotIndex: b,
    subSlotIndex: B
  } = $() || {}, V = i({
    parent: f,
    props: _,
    target: d,
    slot: p,
    slotKey: m,
    slotIndex: b,
    subSlotIndex: B,
    onDestroy(u) {
      a.push(u);
    }
  });
  ve("$$ms-gr-react-wrapper", V), be(() => {
    _.set(A(t));
  }), ye(() => {
    a.forEach((u) => u());
  });
  function J(u) {
    P[u ? "unshift" : "push"](() => {
      o = u, d.set(o);
    });
  }
  function Y(u) {
    P[u ? "unshift" : "push"](() => {
      r = u, p.set(r);
    });
  }
  return n.$$set = (u) => {
    l(17, t = k(k({}, t), T(u))), "svelteInit" in u && l(5, i = u.svelteInit), "$$scope" in u && l(6, s = u.$$scope);
  }, t = T(t), [o, r, d, p, c, i, s, e, J, Y];
}
class Ie extends ce {
  constructor(t) {
    super(), me(this, t, Ce, xe, he, {
      svelteInit: 5
    });
  }
}
const F = window.ms_globals.rerender, C = window.ms_globals.tree;
function Re(n) {
  function t(l) {
    const o = E(), r = new Ie({
      ...l,
      props: {
        svelteInit(e) {
          window.ms_globals.autokey += 1;
          const s = {
            key: window.ms_globals.autokey,
            svelteInstance: o,
            reactComponent: n,
            props: e.props,
            slot: e.slot,
            target: e.target,
            slotIndex: e.slotIndex,
            subSlotIndex: e.subSlotIndex,
            slotKey: e.slotKey,
            nodes: []
          }, c = e.parent ?? C;
          return c.nodes = [...c.nodes, s], F({
            createPortal: I,
            node: C
          }), e.onDestroy(() => {
            c.nodes = c.nodes.filter((i) => i.svelteInstance !== o), F({
              createPortal: I,
              node: C
            });
          }), s;
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
function Se(n) {
  try {
    return typeof n == "string" ? new Function(`return (...args) => (${n})(...args)`)() : void 0;
  } catch {
    return;
  }
}
function Oe(n) {
  return D(() => Se(n), [n]);
}
const ke = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Pe(n) {
  return n ? Object.keys(n).reduce((t, l) => {
    const o = n[l];
    return typeof o == "number" && !ke.includes(l) ? t[l] = o + "px" : t[l] = o, t;
  }, {}) : {};
}
function S(n) {
  const t = [], l = n.cloneNode(!1);
  if (n._reactElement)
    return t.push(I(h.cloneElement(n._reactElement, {
      ...n._reactElement.props,
      children: h.Children.toArray(n._reactElement.props.children).map((r) => {
        if (h.isValidElement(r) && r.props.__slot__) {
          const {
            portals: e,
            clonedElement: s
          } = S(r.props.el);
          return h.cloneElement(r, {
            ...r.props,
            el: s,
            children: [...h.Children.toArray(r.props.children), ...e]
          });
        }
        return null;
      })
    }), l)), {
      clonedElement: l,
      portals: t
    };
  Object.keys(n.getEventListeners()).forEach((r) => {
    n.getEventListeners(r).forEach(({
      listener: s,
      type: c,
      useCapture: i
    }) => {
      l.addEventListener(c, s, i);
    });
  });
  const o = Array.from(n.childNodes);
  for (let r = 0; r < o.length; r++) {
    const e = o[r];
    if (e.nodeType === 1) {
      const {
        clonedElement: s,
        portals: c
      } = S(e);
      t.push(...c), l.appendChild(s);
    } else e.nodeType === 3 && l.appendChild(e.cloneNode());
  }
  return {
    clonedElement: l,
    portals: t
  };
}
function je(n, t) {
  n && (typeof n == "function" ? n(t) : n.current = t);
}
const O = K(({
  slot: n,
  clone: t,
  className: l,
  style: o
}, r) => {
  const e = Q(), [s, c] = X([]);
  return Z(() => {
    var p;
    if (!e.current || !n)
      return;
    let i = n;
    function _() {
      let a = i;
      if (i.tagName.toLowerCase() === "svelte-slot" && i.children.length === 1 && i.children[0] && (a = i.children[0], a.tagName.toLowerCase() === "react-portal-target" && a.children[0] && (a = a.children[0])), je(r, a), l && a.classList.add(...l.split(" ")), o) {
        const f = Pe(o);
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
        } = S(n);
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
  }, [n, t, l, o, r]), h.createElement("react-child", {
    ref: e,
    style: {
      display: "contents"
    }
  }, ...s);
});
function q(n, t) {
  return n.filter(Boolean).map((l) => {
    if (typeof l != "object")
      return l;
    const o = {
      ...l.props
    };
    let r = o;
    Object.keys(l.slots).forEach((s) => {
      if (!l.slots[s] || !(l.slots[s] instanceof Element) && !l.slots[s].el)
        return;
      const c = s.split(".");
      c.forEach((a, f) => {
        r[a] || (r[a] = {}), f !== c.length - 1 && (r = o[a]);
      });
      const i = l.slots[s];
      let _, d, p = !1;
      i instanceof Element ? _ = i : (_ = i.el, d = i.callback, p = i.clone || !1), r[c[c.length - 1]] = _ ? d ? (...a) => (d(c[c.length - 1], a), /* @__PURE__ */ w.jsx(O, {
        slot: _,
        clone: p || (t == null ? void 0 : t.clone)
      })) : /* @__PURE__ */ w.jsx(O, {
        slot: _,
        clone: p || (t == null ? void 0 : t.clone)
      }) : r[c[c.length - 1]], r = o;
    });
    const e = "children";
    return l[e] && (o[e] = q(l[e], t)), o;
  });
}
function Le(n, t) {
  return n ? /* @__PURE__ */ w.jsx(O, {
    slot: n,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function Te({
  key: n,
  setSlotParams: t,
  slots: l
}, o) {
  return (...r) => (t(n, r), Le(l[n], {
    clone: !0,
    ...o
  }));
}
const Ae = Re(({
  slots: n,
  items: t,
  slotItems: l,
  children: o,
  onChange: r,
  setSlotParams: e,
  expandIcon: s,
  ...c
}) => {
  const i = Oe(s);
  return /* @__PURE__ */ w.jsxs(w.Fragment, {
    children: [o, /* @__PURE__ */ w.jsx(ee, {
      ...c,
      onChange: (_) => {
        r == null || r(_);
      },
      expandIcon: n.expandIcon ? Te({
        slots: n,
        setSlotParams: e,
        key: "expandIcon"
      }) : i,
      items: D(() => t || q(l), [t, l])
    })]
  });
});
export {
  Ae as Collapse,
  Ae as default
};
