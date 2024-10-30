export const id=67;export const ids=[67];export const modules={2694:(e,i,t)=>{var a=t(5461),d=t(487),s=t(4258),l=t(8597),n=t(196),o=t(9760),r=t(3167);(0,a.A)([(0,n.EM)("ha-formfield")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,n.MZ)({type:Boolean,reflect:!0})],key:"disabled",value(){return!1}},{kind:"method",key:"render",value:function(){const e={"mdc-form-field--align-end":this.alignEnd,"mdc-form-field--space-between":this.spaceBetween,"mdc-form-field--nowrap":this.nowrap};return l.qy` <div class="mdc-form-field ${(0,o.H)(e)}">
      <slot></slot>
      <label class="mdc-label" @click=${this._labelClick}>
        <slot name="label">${this.label}</slot>
      </label>
    </div>`}},{kind:"method",key:"_labelClick",value:function(){const e=this.input;if(e&&(e.focus(),!e.disabled))switch(e.tagName){case"HA-CHECKBOX":e.checked=!e.checked,(0,r.r)(e,"change");break;case"HA-RADIO":e.checked=!0,(0,r.r)(e,"change");break;default:e.click()}}},{kind:"field",static:!0,key:"styles",value(){return[s.R,l.AH`
      :host(:not([alignEnd])) ::slotted(ha-switch) {
        margin-right: 10px;
        margin-inline-end: 10px;
        margin-inline-start: inline;
      }
      .mdc-form-field {
        align-items: var(--ha-formfield-align-items, center);
        gap: 4px;
      }
      .mdc-form-field > label {
        direction: var(--direction);
        margin-inline-start: 0;
        margin-inline-end: auto;
        padding: 0;
      }
      :host([disabled]) label {
        color: var(--disabled-text-color);
      }
    `]}}]}}),d.M)},2283:(e,i,t)=>{var a=t(5461),d=t(8259),s=t(4414),l=t(8597),n=t(196);(0,a.A)([(0,n.EM)("ha-radio")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",static:!0,key:"styles",value(){return[s.R,l.AH`
      :host {
        --mdc-theme-secondary: var(--primary-color);
      }
    `]}}]}}),d.F)},3024:(e,i,t)=>{t.r(i),t.d(i,{CreateDeviceDialog:()=>h});var a=t(5461),d=t(9534),s=(t(6396),t(2283),t(2694),t(9373),t(3167)),l=t(8597),n=t(196),o=t(8762),r=t(3799),c=t(3688);let h=(0,a.A)([(0,n.EM)("lcn-create-device-dialog")],(function(e,i){class t extends i{constructor(...i){super(...i),e(this)}}return{F:t,d:[{kind:"field",decorators:[(0,n.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.MZ)({attribute:!1})],key:"lcn",value:void 0},{kind:"field",decorators:[(0,n.wk)()],key:"_params",value:void 0},{kind:"field",decorators:[(0,n.wk)()],key:"_isGroup",value(){return!1}},{kind:"field",decorators:[(0,n.wk)()],key:"_segmentId",value(){return 0}},{kind:"field",decorators:[(0,n.wk)()],key:"_addressId",value(){return 5}},{kind:"field",decorators:[(0,n.wk)()],key:"_invalid",value(){return!1}},{kind:"method",key:"showDialog",value:async function(e){this._params=e,this.lcn=e.lcn,await this.updateComplete}},{kind:"method",key:"firstUpdated",value:function(e){(0,d.A)(t,"firstUpdated",this,3)([e]),(0,c.W)()}},{kind:"method",key:"willUpdate",value:function(e){e.has("_invalid")&&(this._invalid=!this._validateSegmentId(this._segmentId)||!this._validateAddressId(this._addressId,this._isGroup))}},{kind:"method",key:"render",value:function(){return this._params?l.qy`
      <ha-dialog
        open
        scrimClickAction
        escapeKeyAction
        .heading=${(0,o.l)(this.hass,this.lcn.localize("dashboard-devices-dialog-create-title"))}
        @closed=${this._closeDialog}
      >
        <div id="type">${this.lcn.localize("type")}</div>

        <ha-formfield label=${this.lcn.localize("module")}>
          <ha-radio
            name="is_group"
            value="module"
            .checked=${!1===this._isGroup}
            @change=${this._isGroupChanged}
          ></ha-radio>
        </ha-formfield>

        <ha-formfield label=${this.lcn.localize("group")}>
          <ha-radio
            name="is_group"
            value="group"
            .checked=${!0===this._isGroup}
            @change=${this._isGroupChanged}
          ></ha-radio>
        </ha-formfield>

        <ha-textfield
          .label=${this.lcn.localize("segment-id")}
          type="number"
          .value=${this._segmentId.toString()}
          min="0"
          required
          autoValidate
          @input=${this._segmentIdChanged}
          .validityTransform=${this._validityTransformSegmentId}
          .validationMessage=${this.lcn.localize("dashboard-devices-dialog-error-segment")}
        ></ha-textfield>

        <ha-textfield
          .label=${this.lcn.localize("id")}
          type="number"
          .value=${this._addressId.toString()}
          min="0"
          required
          autoValidate
          @input=${this._addressIdChanged}
          .validityTransform=${this._validityTransformAddressId}
          .validationMessage=${this._isGroup?this.lcn.localize("dashboard-devices-dialog-error-group"):this.lcn.localize("dashboard-devices-dialog-error-module")}
        ></ha-textfield>

        <div class="buttons">
          <mwc-button
            slot="secondaryAction"
            @click=${this._closeDialog}
            .label=${this.lcn.localize("dismiss")}
          ></mwc-button>

          <mwc-button
            slot="primaryAction"
            @click=${this._create}
            .disabled=${this._invalid}
            .label=${this.lcn.localize("create")}
          ></mwc-button>
        </div>
      </ha-dialog>
    `:l.s6}},{kind:"method",key:"_isGroupChanged",value:function(e){this._isGroup="group"===e.target.value}},{kind:"method",key:"_segmentIdChanged",value:function(e){const i=e.target;this._segmentId=+i.value}},{kind:"method",key:"_addressIdChanged",value:function(e){const i=e.target;this._addressId=+i.value}},{kind:"method",key:"_validateSegmentId",value:function(e){return 0===e||e>=5&&e<=128}},{kind:"method",key:"_validateAddressId",value:function(e,i){return e>=5&&e<=254}},{kind:"get",key:"_validityTransformSegmentId",value:function(){return e=>({valid:this._validateSegmentId(+e)})}},{kind:"get",key:"_validityTransformAddressId",value:function(){return e=>({valid:this._validateAddressId(+e,this._isGroup)})}},{kind:"method",key:"_create",value:async function(){const e={name:"",address:[this._segmentId,this._addressId,this._isGroup]};await this._params.createDevice(e),this._closeDialog()}},{kind:"method",key:"_closeDialog",value:function(){this._params=void 0,(0,s.r)(this,"dialog-closed",{dialog:this.localName})}},{kind:"get",static:!0,key:"styles",value:function(){return[r.nA,l.AH`
        #port-type {
          margin-top: 16px;
        }
        ha-textfield {
          display: block;
          margin-bottom: 8px;
        }
        .buttons {
          display: flex;
          justify-content: space-between;
          padding: 8px;
        }
      `]}}]}}),l.WF)}};
//# sourceMappingURL=6H1vYP7l.js.map