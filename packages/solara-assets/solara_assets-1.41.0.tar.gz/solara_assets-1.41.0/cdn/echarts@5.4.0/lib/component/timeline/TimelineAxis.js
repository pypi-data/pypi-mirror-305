
/*
* Licensed to the Apache Software Foundation (ASF) under one
* or more contributor license agreements.  See the NOTICE file
* distributed with this work for additional information
* regarding copyright ownership.  The ASF licenses this file
* to you under the Apache License, Version 2.0 (the
* "License"); you may not use this file except in compliance
* with the License.  You may obtain a copy of the License at
*
*   http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing,
* software distributed under the License is distributed on an
* "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
* KIND, either express or implied.  See the License for the
* specific language governing permissions and limitations
* under the License.
*/


/**
 * AUTO-GENERATED FILE. DO NOT MODIFY.
 */

/*
* Licensed to the Apache Software Foundation (ASF) under one
* or more contributor license agreements.  See the NOTICE file
* distributed with this work for additional information
* regarding copyright ownership.  The ASF licenses this file
* to you under the Apache License, Version 2.0 (the
* "License"); you may not use this file except in compliance
* with the License.  You may obtain a copy of the License at
*
*   http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing,
* software distributed under the License is distributed on an
* "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
* KIND, either express or implied.  See the License for the
* specific language governing permissions and limitations
* under the License.
*/
import { __extends } from "tslib";
import Axis from '../../coord/Axis.js';
/**
 * Extend axis 2d
 */

var TimelineAxis =
/** @class */
function (_super) {
  __extends(TimelineAxis, _super);

  function TimelineAxis(dim, scale, coordExtent, axisType) {
    var _this = _super.call(this, dim, scale, coordExtent) || this;

    _this.type = axisType || 'value';
    return _this;
  }
  /**
   * @override
   */


  TimelineAxis.prototype.getLabelModel = function () {
    // Force override
    return this.model.getModel('label');
  };
  /**
   * @override
   */


  TimelineAxis.prototype.isHorizontal = function () {
    return this.model.get('orient') === 'horizontal';
  };

  return TimelineAxis;
}(Axis);

export default TimelineAxis;