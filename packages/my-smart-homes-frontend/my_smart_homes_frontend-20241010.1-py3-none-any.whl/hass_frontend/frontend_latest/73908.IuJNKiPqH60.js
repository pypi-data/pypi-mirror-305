export const id=73908;export const ids=[73908];export const modules={77372:(t,e,a)=>{var s=a(36312),i=a(72606),n=a(15112),o=a(77706),r=a(49141);(0,s.A)([(0,o.EM)("ha-button")],(function(t,e){return{F:class extends e{constructor(...e){super(...e),t(this)}},d:[{kind:"field",static:!0,key:"styles",value:()=>[r.R,n.AH`::slotted([slot=icon]){margin-inline-start:0px;margin-inline-end:8px;direction:var(--direction);display:block}.mdc-button{height:var(--button-height,36px)}.trailing-icon{display:flex}.slot-container{overflow:var(--button-slot-container-overflow,visible)}`]}]}}),i.Button)},73908:(t,e,a)=>{var s=a(36312),i=a(15112),n=a(77706),o=a(40368),r=(a(77372),a(41026)),d=a(20101);(0,s.A)([(0,n.EM)("ha-toast")],(function(t,e){return{F:class extends e{constructor(...e){super(...e),t(this)}},d:[{kind:"field",static:!0,key:"styles",value:()=>[d.R,i.AH`
      .mdc-snackbar--leading {
        justify-content: center;
      }

      .mdc-snackbar {
        margin: 8px;
        right: calc(8px + env(safe-area-inset-right));
        bottom: calc(8px + env(safe-area-inset-bottom));
        left: calc(8px + env(safe-area-inset-left));
      }

      .mdc-snackbar__surface {
        min-width: 350px;
        max-width: 650px;
      }

      // Revert the default styles set by mwc-snackbar
      @media (max-width: 480px), (max-width: 344px) {
        .mdc-snackbar__surface {
          min-width: inherit;
        }
      }

      @media all and (max-width: 450px), all and (max-height: 500px) {
        .mdc-snackbar {
          right: env(safe-area-inset-right);
          bottom: env(safe-area-inset-bottom);
          left: env(safe-area-inset-left);
        }
        .mdc-snackbar__surface {
          min-width: 100%;
        }
      }
    `]}]}}),r.q);let c=(0,s.A)(null,(function(t,e){return{F:class extends e{constructor(...e){super(...e),t(this)}},d:[{kind:"field",decorators:[(0,n.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.wk)()],key:"_parameters",value:void 0},{kind:"field",decorators:[(0,n.P)("ha-toast")],key:"_toast",value:void 0},{kind:"method",key:"showDialog",value:async function(t){t.id&&this._parameters?.id===t.id||this._toast?.close(),t&&0!==t.duration?(this._parameters=t,(void 0===this._parameters.duration||this._parameters.duration>0&&this._parameters.duration<=4e3)&&(this._parameters.duration=4e3),await this.updateComplete,this._toast?.show()):this._parameters=void 0}},{kind:"method",key:"_toastClosed",value:function(){this._parameters=void 0}},{kind:"method",key:"render",value:function(){return this._parameters?i.qy` <ha-toast leading dir="${(0,o.qC)(this.hass)?"rtl":"ltr"}" .labelText="${this._parameters.message}" .timeoutMs="${this._parameters.duration}" @MDCSnackbar:closed="${this._toastClosed}"> ${this._parameters?.action?i.qy` <ha-button slot="action" .label="${this._parameters?.action.text}" @click="${this.buttonClicked}"></ha-button> `:i.s6} ${this._parameters?.dismissable?i.qy` <ha-icon-button .label="${this.hass.localize("ui.common.close")}" .path="${"M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z"}" dialogAction="close" slot="dismiss"></ha-icon-button> `:i.s6} </ha-toast> `:i.s6}},{kind:"method",key:"buttonClicked",value:function(){this._toast?.close("action"),this._parameters?.action&&this._parameters?.action.action()}}]}}),i.WF);customElements.define("notification-manager",c)}};
//# sourceMappingURL=73908.IuJNKiPqH60.js.map