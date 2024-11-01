#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : ecraft
# @Time         : 2024/10/31 16:30
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :

from meutils.pipe import *
from meutils.io.files_utils import to_url
from meutils.schemas.image_types import ImageRequest, ImagesResponse, RecraftImageRequest
from meutils.notice.feishu import IMAGES, send_message as _send_message
from meutils.config_utils.lark_utils import get_next_token_for_polling
from meutils.decorators.retry import retrying

BASE_URL = "https://api.recraft.ai"

FEISHU_URL = "https://xchatllm.feishu.cn/sheets/GYCHsvI4qhnDPNtI4VPcdw2knEd?sheet=Lrhtf2"

DEFAULT_MODEL = "recraftv3"
MODELS = {}

send_message = partial(
    _send_message,
    title=__name__,
    url=IMAGES
)


@alru_cache(ttl=10 * 60)
@retrying()
async def get_access_token(token: Optional[str] = None):
    token = token or await get_next_token_for_polling(feishu_url=FEISHU_URL)
    headers = {"cookie": token}

    async with httpx.AsyncClient(base_url="https://www.recraft.ai", headers=headers, timeout=60) as client:
        response = await client.get("/api/auth/session")
        response.raise_for_status()
        logger.debug(response.json())
        return response.json()["accessToken"]


@retrying()
async def generate(request: RecraftImageRequest, token: Optional[str] = None):
    token = await get_access_token(token)
    headers = {"Authorization": f"Bearer {token}"}
    # params = {"project_id": "26016b99-3ad0-413b-821b-5f884bd9454e"}  # project_id 是否是必要的
    params = {}  # project_id 是否是必要的
    # params = {"project_id": "47ba6825-0fde-4cea-a17e-ed7398c0a298"}
    payload = request.model_dump(exclude_none=True)
    logger.debug(payload)

    async with httpx.AsyncClient(base_url=BASE_URL, headers=headers, timeout=60) as client:
        response = await client.post(f"/queue_recraft/prompt_to_image", params=params, json=payload)
        response.raise_for_status()
        params = {
            "operation_id": response.json()["operationId"]
        }
        logger.debug(params)

        response = await client.get("/poll_recraft", params=params)
        response.raise_for_status()
        metadata = response.json()
        logger.debug(metadata)

        # {'credits': 1,
        #  'height': 1024,
        #  'images': [{'image_id': 'f9d8e7dd-c31f-4208-abe4-f44cdff050c2',
        #              'image_invariants': {'preset': 'any'},
        #              'transparent': False,
        #              'vector_image': False}],
        #  'random_seed': 1423697946,
        #  'request_id': '77bd917d-0960-4921-916f-038c773a41fd',
        #  'transform_model': 'recraftv3',
        #  'width': 1024}

        params = {"raster_image_content_type": "image/webp"}  #####

        images = []
        for image in response.json()["images"]:
            response = await client.get(f"""/image/{image["image_id"]}""", params=params)
            url = await to_url(response.content)
            images.append(url)

        return ImagesResponse(image=images, metadata=metadata)


@alru_cache(ttl=10 * 60)
async def check_token(token, threshold: float = 1):
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient(base_url=BASE_URL, headers=headers, timeout=60) as client:
        response = await client.get("/users/me")
        response.raise_for_status()
        return response.json()["credits"] >= threshold


if __name__ == '__main__':
    token = "AMP_7268c9db0f=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI2OTE1YzI1My1jMTJjLTQ5ODYtYjM3Ni0xMTI3Y2ZmMTFlMjglMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjI5MjQ1NTQ0Yy1lNzUwLTQ1MGEtYWMyZi1mMTU3YTBiMjRiMTglMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzMwMzY1NzE0NjE2JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTczMDM3MDQ3NTE1MyUyQyUyMmxhc3RFdmVudElkJTIyJTNBMzQ4JTJDJTIycGFnZUNvdW50ZXIlMjIlM0EzNiU3RA==;__zlcmid=1OVn8OoYVNvKEWM;AMP_MKTG_7268c9db0f=JTdCJTdE;_ga=GA1.1.435165527.1730362257;__Secure-next-auth.session-token.1=m8UCvC8TIMOIb__wBsUhw5jiWe8GxrS0NX5TJ2tsoXyAYek6R9WOpqwQxSXWdPkI8s7QcQ_uCOq9ePRJMvFd9kOZobxMV2OMgWGAGcFwosdGDX0DXHp-T1EobYLt_lQ4NerfCPIg-OoV9_c-bpfPLkL_2aaf11Vq8mTgV8SN6Rj_3FUm2VSWN249CCK7-awqseMTYar7vSEXrL7HyY5IuVirHssWMyaCoLpR227FDCdFVs95h57sHwdhvgoLnkyva8efxHLH1dtXM-AytPfkRMUV1NJy-0lugSg2ufQVg8C_m3tLojfvv1fpFqmtIOG1n64-Vc4RDUR3FStJM1Ln0_IwmcNzjF9A2__b2KRMvEo7_XkNBRgFuJ0CRdwngQhmQELZkyCjc6Ft-7FlzbQopmhzNDfNqKaZVrYMhLffHX9wl.gNGnYIFn_rsTu-Zib4hO2g;_uetsid=a8a77260975f11ef834045ac9f7830ad;__Host-next-auth.csrf-token=78920fc4c6bf5aef5c2063e3a4397b1e41074713e35020cf7049156e02d53355%7C2c8e6897101210b68ba31cec5c6232d8ab76a3e070cda7b82ad051680ab93fe0;_ga_ME15C3DGRL=GS1.1.1730365714.2.1.1730370460.0.0.0;_fbp=fb.1.1730362257600.714008794112161913;_pin_unauth=dWlkPU0yWmxPR1JsWkRJdE5qZGlZeTAwTWpNeUxXRmpNVEV0TlRrd1l6RTNZelEwTldZMw;__stripe_sid=4b4e2934-1303-4190-b7f3-9b2a667c83d8f37da3;x-recraft-referral-code=3h7wfOgFGn;__Secure-next-auth.callback-url=https%3A%2F%2Fwww.recraft.ai%2Fprojects;__Secure-next-auth.session-token.0=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..xUYQ441xB7cnocd3.enGv6U_1rMwexl_hbGpP1E5GXNYgFpond3pxkS3Udf5QkUZ5nXV2VE4L2ZoPz64o0dCXUSUOv_4j9Mhb2eDwo7lmtItoBkJ8fH3SpnmGzfW6LV21lQ3GgXN_FSY4Nf74UHavhzz_vNDTr5DvfINNu_3OBi_lge0xeCfW9Ewsti69523YTq9ppOPLyTBVPI7BEmHX3PWpLUXuCJdoBbwD3ytBm3I01GfOpm-lltgsHlnE-37AXZhHXp5Yt6ZYwod5TVz1Jcui-9sNkQ-zsRCEM2hsk2u471niXw7blf59Wr1-Tl7e8jB-aIEeE3iewIZqmWmKvrx6WvgJ8JQuiZ0TU38sosDnE7yrMQP3_vMKKmY0zkKw-m0omi9wGKTb-rgz1ZjfP3vDzBo1r0NRYneVxyF6-17Q8JmORlxYr7ORMVI6xaUcIB0Pti62FzuIdGUtXjqzzppn5MG3ItW-0PPOrVRVBYNSaKAga8tQDq6wzkyperyLkK-vPYzIxRehM3iAYL85GcfYv58-NiAipgKFazieeVsKs8MxayV2zkWSl3EOE7wCT1Y14CElvQYo23Fvl_BtKcVXDTDY_MZq9tWH0VIuuVW7cGKr5_SMt8MSRkQ0wiE6lPWWh0PzxvzvCUJE7joJRY3_jxIWT2jHZVYq3lxetbtiA5EmOjnYlNinmVonHdtD6drVYenfAnPjPN6M0MiMS1W9Gb0HKk3xhWzm2zHNRnynS8b8hRWN5-Ne3HI5DGOHl2HxF2UUfyR7QQ9EOEJNyrjDBsunK2BLD0sh7xx85iXk_2VfRLZlOr8KKXf6PmSBNE49p9lc9Pm6bazofmclr0MogLhNiRHGP5OZWZPZTiFDTKNp1GmsFeVeiyIQTM_61d7frSXQlDvljmj9inGVldOn_hH60hyLKAnXgS4BuCwWQ4S6sGnwYH_iKP6WNUpj9cTt0d3PWX1oV8iEcqJQLIHPqq3cbvkw5FpMR2Vq0EMLmN9hcQXKH7C64R7EjZdz5Ee7i3tW3LckIYA35nXawjmkX0Wu2RbMIfrc5Efy0LdF1s9AxKKPZ4Co5vq999XsWeTbX6nI299rbTCSZ38H5txH9x-pWmqvkstmhc4nB6DoRx7uqx2YTpWFtDiwhIMYUvlj8EWsSzp3rkfQJRpNegUYJG3gK9YZNB1SBS_GYd_I69E6a6EuItJzfqI-HKvp8bvhkzvYo4vZBuolSmO2y3OM6RlDqxwQeqyv9L7SbOhZuJg1PtUYGNSrFTP_JRqbsgaG1fK9Wm1ftLKbXkKlyYtVZ0g4NFvV-mI7E7RMFneCiyzY8FuzVvoDrEN6vxadEJ2_-Jzfnonv0ZfX557hd_7rZDRuFAw5KXYXBFe1X13CWs01VBN58LNAABRnuYpmOW9TbYhn9XdBgY6Hz2Y9k4lt3IwL3nXCKp3Txw4AZFN5he0Phy6xpeaWYuNEmmhKeK2lLxhrBQUtr2h_VFzc3_GOsflnpO3S3ebT5T53Gsc5t6Walmv4_1_pAHjUo1SjEuDP9NgwZfLK9VLQRWYryKoRks36FV8tjcZNznfrbq6HLfpxcbbcO7Sryhb1HSoGIQvMFkYy69n6dgufZxT_pwHg6ARgJWY3Y7UFWCmohj2UAmghlm9MBGkywdSbvZmsVMd-nj0ppXxfw14k4xVw5QRXTd72tSD_GMob96M31WZPMa77uaorSNcODiUNBAzfaVYVDDOcGY5Sq9YcwEk3mT_P-GWskVgulBsR3QudBF32Rb6Y3AcOu-2VyDxReU74UrivQmLMJ7vifoSFnOXiZr5hDzQjRtQzQWkrDYFdGhFFcPuQKHixYv9XYfTt6ssmsG9P_5IS--cTMwfxPDMbDJd4wVXLu7t9cfplxEThp9Y5lq_s3mVFvGKLb7XtnAQ5Jkx0lwIjldcL45tFxY_s-PcQgEzjDtR6G-f7nscpErSNCJ1A1EIJza4qJ_fGJwCwMC9Y1Zyr5Oi1MOMuc2HTp3wHL6kgB4eC_B9y5ICJ5nrq5FqjTwXqYCfEZMZnNQsFun9l69LElWvZG-2QD0Mg6SpNSFlSIqAz4PcWlRFIC1fSzcfQkFOfQF1jlMaVKRW0X6EHD9a231bPPcL3oL3GjfypwlWEXx7VoP0yW7nV9lSCtP4H4I3cLjTcDkH49QBY9X45qIjCgFpEVuJs5tqW4x19nu9KZUSbYzu4Kez6K4DhaL8Aeh4dO_nZA-RgKBAbvXPf4VrMmFO_O-08uUlUtZw8eOQQlb1PnHGzq0NcvdvB_Xiec3EdwxuYz7bT-JQq-5IpiLKwD6X8kVOMH3OY3TkQITfih5PzZmJkoS5kKwdjiaoAfO2QzQWeRUxOSAm8ijsIeFIRDOuhWz2qg0cGeZb7JqTXr7H6PPjA4OONhAZUHLB1FDsmyoYp90KpeVsKiFD1KVPSVv3rN3ibbkeDTeoqhlfkB_EXWZEt0nME8tODje2nCvCI9paGueUvcABS5Qu4vK3KhMmkuntvtplnbY_ufi4wHQrr7mIvZC2sRY66tKF1pLZ7c4wSjPHplNgX49BrkRlvnCCIVn3piZmu2erwGt2N_qH1luTFXLu2c1FKWVwPQcachWyoxMwxNEscYLsHFyA46eQeUf3zkiwsGl9nsQOZnNVjhgH1Mh84X5QIV9-e6ludjV1s-lNmOajI7J8sxl6W4wSN0AJD-D25TUaLXwv-Sk9cs_OpqhQe5K2oBFNg4OMWL7gI2G7jKBFZ_yG_vfEIdLQ2N3kwmLwBlzuImiQhAmJuLbWFFODm9ZsD6abngzr_Gr9gicf4KW-6h55YeB_iUPwxboQxyrlBBP6Ua33rUwIWlLOktLE0s8PgdwB9kZ4d0YBZFRsvlDDXV6ttFKDO4PLtAOTsnpQbS7O-v2_FHoKeWxu9a9qyb-ATjagX5IdVyyHA85yU7Ufmv25G4ecY6_PSdoMmz2n1T7bw_4KDkjCyCjukL-v9akntugn_WBsWKZ5gohkZoPgijqHBlRAAD3xzbg2ZOj6YV4y0UT8WOFC27qJDI8PhHYO1zNlKI7atYPGR6toHHVej-4Vjj4mGaiLarmTrc8sLei4yodj5Xx1ojnP4N0wwYWMwEldlbKEC_xMeYyCXUmob0y2wQkZ_yH4cLyZqDShgHk6Nu387QMLKVH51zPAuN9l50SswVR0sU0SBNAi6wvyhKwOfEV1c1DpTFW8cAi4D3DG5i9VGgRkRvbh7AOhc6TlSg4wLpeRlo0vemTBfgUR0yTc7ZRSmOAaafChqdkY39DPfgHCBNTh6W5kspoci4dMY5NaBDUO3Ejk7TpkC26IawAjxhrDyMeQIWIBphJwfqScwfvmZD9YmsyIkocJSbh84oVo6mmlLwI23_6yTdUxdWcudy9-FunfB0s7CIxslcRgjn_oHpUYgu5Dnp_wF_Jd_zqNihDoiRCy0uJL8f97ohEs9DfPRI-t-AscIXpj8xqdfHGo0StFmX58-ExLCFpVRBoScN_ycd3wVCydj9znRY_JbM93MJUNgPD0b9EuTUS8VKLU2SH_1cMC2PQDFwpgBhj1qcHWqgvcrIxeNCUMqjY6j4Yuu-jvyg7CCvwvDjwfcHXAqtAGltdkw0Duc728orkY9CjQa1ITtUHUuZ03LMDFb2RA3hrEqewIJFciYZ3X_Jb3ZQuZhh-AujA6j5ptvcchFE8ack0ZitAadtflk98tJXBZSwxBsCdKIYMRTFfXbGOYZNTTFyVVNLiTrXVtKJfkFBoPbqXm675H1M4WMPqnZ9_eUE1dsOVLIckK2NQ8pDMoSnY6Ys18HGlW19bZq1IO5ahRNUeDYkk_jWsQ_OESkYpN9mBPEVOVGlhvWNBCBG7pfBdj2Hm5OaX2y_7zobM4ze4h;__stripe_mid=d21b2291-edb8-4cb1-8fac-05c6a9493ca8d85a3c;_clck=uflztg%7C2%7Cfqh%7C0%7C1765;_clsk=e1belg%7C1730370462237%7C61%7C1%7Cj.clarity.ms%2Fcollect;_gcl_au=1.1.906962865.1730362257;_tt_enable_cookie=1;_ttp=412qSInHGw3jjdyNR6K4tBIYmNZ;_uetvid=a8a766f0975f11ef9b7921e48a0cd258"
    token= None
    # arun(get_access_token())
    request = RecraftImageRequest(
        prompt='一条猫'
    )
    arun(generate(request, token=token))
