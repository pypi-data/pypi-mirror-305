# Copyright (c) 2024, Zhendong Peng (pzd17@tsinghua.org.cn)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import click
from speaker_diarization import SpeakerDiarization


@click.command()
@click.argument("in_wav", type=click.Path(exists=True, file_okay=True))
def main(in_wav):
    sd = SpeakerDiarization()
    for result in sd.process(in_wav):
        print(result)


if __name__ == "__main__":
    main()
