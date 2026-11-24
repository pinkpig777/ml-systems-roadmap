import json, platform, torch
print(json.dumps(dict(os=platform.platform(), python=platform.python_version(), torch=torch.__version__, cuda=torch.version.cuda, gpu=[dict(name=p.name, vram_bytes=p.total_memory) for p in [torch.cuda.get_device_properties(i) for i in range(torch.cuda.device_count())]]), indent=2))
