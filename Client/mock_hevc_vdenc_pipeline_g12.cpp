/*===================== begin_copyright_notice ==================================

INTEL CONFIDENTIAL
Copyright 2018
Intel Corporation All Rights Reserved.

The source code contained or described herein and all documents related to the
source code ("Material") are owned by Intel Corporation or its suppliers or
licensors. Title to the Material remains with Intel Corporation or its suppliers
and licensors. The Material contains trade secrets and proprietary and confidential
information of Intel or its suppliers and licensors. The Material is protected by
worldwide copyright and trade secret laws and treaty provisions. No part of the
Material may be used, copied, reproduced, modified, published, uploaded, posted,
transmitted, distributed, or disclosed in any way without Intel's prior express
written permission.

No license under any patent, copyright, trade secret or other intellectual
property right is granted to or conferred upon you by disclosure or delivery
of the Materials, either expressly, by implication, inducement, estoppel
or otherwise. Any license under such intellectual property rights must be
express and approved by Intel in writing.

======================= end_copyright_notice ==================================*/

//!
//! \file     mock_hevc_vdenc_pipeline_g12.cpp
//! \brief    implementation file of HevcVdencPipelineG12Mock class
//! \a mock derived from mock_hevc_vdenc_pipeline_g12 and used for ult test
//!


namespace encode 
{
        void HevcVdencPipelineG12Mock::set_m_brcHistoryBufSize(uint32_t m_brcHistoryBufSize_mock)
        {
            m_brcHistoryBufSize = m_brcHistoryBufSize_mock;
        }
}
