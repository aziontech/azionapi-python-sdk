from data_streaming.paths.data_streaming_streamings_data_streaming_id.get import ApiForget
from data_streaming.paths.data_streaming_streamings_data_streaming_id.put import ApiForput
from data_streaming.paths.data_streaming_streamings_data_streaming_id.delete import ApiFordelete
from data_streaming.paths.data_streaming_streamings_data_streaming_id.patch import ApiForpatch


class DataStreamingStreamingsDataStreamingId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
