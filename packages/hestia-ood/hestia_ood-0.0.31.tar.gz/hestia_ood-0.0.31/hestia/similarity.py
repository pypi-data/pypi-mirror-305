from multiprocessing import cpu_count
import os
import shutil
import subprocess
import time
from typing import Callable, List, Optional, Union

import numpy as np
import pandas as pd
from tqdm import tqdm
import scipy.sparse as spr
from concurrent.futures import ThreadPoolExecutor

from hestia.utils import BULK_SIM_METRICS


SUPPORTED_FPS = ['ecfp', 'mapc', 'maccs']


def sim_df2mtx(sim_df: pd.DataFrame,
               size_query: Optional[int] = None,
               size_target: Optional[int] = None,
               threshold: Optional[float] = 0.0,
               filter_smaller: Optional[bool] = True,
               boolean_out: Optional[bool] = True) -> spr.csr_matrix:
    if size_query is None:
        size_query = len(sim_df['query'].unique())
    if size_target is None:
        size_target = size_query

    dtype = np.bool_ if boolean_out else sim_df.metric.dtype
    if filter_smaller:
        sim_df = sim_df[sim_df.metric > threshold]
    else:
        sim_df = sim_df[sim_df.metric < threshold]

    if dtype == np.float16:
        dtype = np.float32

    queries = sim_df['query'].to_numpy()
    targets = sim_df['target'].to_numpy()
    metrics = sim_df['metric'].to_numpy()
    if boolean_out:
        if filter_smaller:
            metrics[metrics > threshold] = True
        else:
            metrics[metrics < threshold] = True
    mtx = spr.coo_matrix((metrics, (queries, targets)),
                         shape=(size_query, size_target),
                         dtype=dtype)
    return mtx.maximum(mtx.transpose())


def calculate_similarity(
    df_query: Union[pd.DataFrame, np.ndarray],
    df_target: Optional[Union[pd.DataFrame, np.ndarray]] = None,
    data_type: str = 'protein',
    similarity_metric: Union[str, Callable] = 'mmseqs+prefilter',
    field_name: str = 'sequence',
    threshold: float = 0.,
    threads: int = cpu_count(),
    verbose: int = 0,
    save_alignment: bool = False,
    filename: str = None,
    distance: str = 'tanimoto',
    bits: int = 1024,
    radius: int = 2,
    denominator: str = 'shortest',
    representation: str = '3di+aa',
    config: dict = None,
    **kwargs
) -> pd.DataFrame:
    """Calculate similarity between entities in
    `df_query` and `df_target`. Entities can be
    biological sequences (nucleic acids or proteins),
    protein structures or small molecules (in SMILES format).

    :param df_query: DataFrame with query entities to calculate similarities
    :type df_query: pd.DataFrame
    :param df_target: DataFrame with target entities to calculate
    similarities. If not specified, the `df_query` will be used as `df_target`
    as well, defaults to None
    :type df_target: pd.DataFrame, optional
    :param data_type: Biochemical data_type to which the data belongs.
    Options: `protein`, `DNA`, `RNA`, or `small_molecule`; defaults to
    'protein'
    :type data_type: Union[str, Callable], optional
    :param similarity_metric: Similarity function to use.
    Options:
        - `protein`: `mmseqs` (local alignment),
          `mmseqs+prefilter` (fast local alignment), `needle` (global
           alignment), or `foldseek` (structural alignment).
        - `DNA` or `RNA`: `mmseqs` (local alignment),
          `mmseqs+prefilter` (fast local alignment), or `needle`
          (global alignment).
        - `small molecule`: `ecfp` (ECFP extended connectivity
        fingerprints), `map4` (MAP4 chiral fingerprint), or `maccs`
        - It can also be a custom made function. It has to fulfill three requirements
          1) be symmetrical, 2) be normalised in the interval [0, 1], 3) f(x_i, x_i) = 1.
          It should support all values within the SimilarityArguments object. If
          it requires additional inputs they can be added to this wrapper function as
          key=value options at the end.
    Defaults to `mmseqs+prefilter`.
    :type similarity_metric: str, optional
    :param field_name: Name of the field with the entity information
    (e.g., `protein_sequence` or `structure_path`), defaults to 'sequence'.
    :type field_name: str, optional
    :param threshold: Similarity value above which entities will be
    considered similar, defaults to 0.3
    :type threshold: float, optional
    :param threads: Number of threads available for parallalelization,
    defaults to cpu_count()
    :type threads: int, optional
    :param verbose: How much information will be displayed.
    Options:
        - 0: Errors,
        - 1: Warnings,
        - 2: All
    Defaults to 0
    :type verbose: int, optional
    :param save_alignment: Save file with similarity calculations,
    defaults to False
    :type save_alignment: bool, optional
    :param filename: Filename where to save the similarity calculations
    requires `save_alignment` set to `True`, defaults to None
    :type filename: str, optional
    :param distance: Distance metrics for small molecule comparison.
    Currently, it is restricted to Tanimoto distance will
    be extended in future patches; if interested in a specific
    metric please let us know.
    Options:
        - `tanimoto`: Calculates the Tanimoto distance
    Defaults to 'tanimoto'.
    :type distance: str, optional
    :param bits: Number of bits for ECFP, defaults to 1024
    :type bits: int, optional
    :param radius: Radius for ECFP calculation, defaults to 2
    :type radius: int, optional
    :param denominator: Denominator for sequence alignments, refers
    to which lenght to be used as denominator for calculating
    the sequence identity.
    Options:
        - `shortest`: The shortest sequence of the pair
        - `longest`: The longest sequence of the pair 
                    (recomended only for peptides)
        - `n_aligned`: Full alignment length 
                      (recomended with global alignment)
    Defaults to 'shortest'
    :type denominator: str, optional
    :param representation: Representation for protein structures
    as interpreted by `Foldseek`.
    Options:
        - `3di`: 3D interactions vocabulary.
        - `3di+aa`: 3D interactions vocabulary and amino
                    acid sequence.
        - `TM`: global structural alignment (slow)
    Defaults to '3di+aa'
    :type representation: str, optional
    :param config: Dictionary with options for EMBOSS needle module
    Default values:
        - "gapopen": 10,
        - "gapextend": 0.5,
        - "endweight": True,
        - "endopen": 10,
        - "endextend": 0.5,
        - "matrix": "EBLOSUM62"
    :type config: dict, optional
    :raises NotImplementedError: Biochemical data_type is not supported
                                 see `data_type`.
    :raises NotImplementedError: Similarity metric is not supported
                                 see `similarity_algorithm`
    :return: DataFrame with similarities (`metric`) between
    `query` and `target`.
    `query` and `target` are named as the indexes obtained from the 
    `pd.unique` function on the corresponding input DataFrames.
    :rtype: pd.DataFrame
    """
    mssg = f'Alignment method: {similarity_metric} '
    mssg += f'not implemented for data_type: {data_type}'
    mssg2 = f'data_type: {data_type} not supported'

    if isinstance(similarity_metric, Callable):
        sim_df = similarity_metric(
            df_query=df_query,
            df_target=df_target,
            field_name=field_name,
            threshold=threshold,
            threads=threads,
            prefilter=False,
            denominator=denominator,
            is_nucleotide=False,
            verbose=verbose,
            save_alignment=save_alignment,
            filename=filename,
            **kwargs
        )
    elif similarity_metric == 'embedding':
        if 'to_df' not in kwargs:
            kwargs['to_df'] = False
        sim_df = _embedding_distance(
            query_embds=df_query, target_embds=df_target,
            distance=distance, threads=threads,
            save_alignment=save_alignment, filename=filename,
            to_df=kwargs['to_df']
        )
    else:
        if 'protein' in data_type:
            if 'mmseqs' in similarity_metric:
                sim_df = _mmseqs2_alignment(
                    df_query=df_query,
                    df_target=df_target,
                    field_name=field_name,
                    threshold=threshold,
                    threads=threads,
                    prefilter='prefilter' in similarity_metric,
                    denominator=denominator,
                    is_nucleotide=False,
                    verbose=verbose,
                    save_alignment=save_alignment,
                    filename=filename
                )
            elif similarity_metric == 'needle':
                sim_df = _needle_alignment(
                    df_query=df_query,
                    df_target=df_target,
                    field_name=field_name,
                    threshold=threshold,
                    threads=threads,
                    is_nucleotide=False,
                    verbose=verbose,
                    config=config,
                    save_alignment=save_alignment,
                    filename=filename
                )
            elif similarity_metric == 'foldseek':
                sim_df = _foldseek_alignment(
                    df_query=df_query,
                    df_target=df_target,
                    field_name=field_name,
                    threshold=threshold,
                    prefilter=False,
                    denominator=denominator,
                    representation=representation,
                    threads=threads,
                    verbose=verbose,
                    save_alignment=save_alignment,
                    filename=filename
                )
            else:
                mssg = f'Alignment method: {similarity_metric} '
                mssg += f'not implemented for data_type: {data_type}'
                raise NotImplementedError(mssg)
        elif data_type.upper() == 'DNA' or data_type.upper() == 'RNA':
            if 'mmseqs' in similarity_metric:
                sim_df = _mmseqs2_alignment(
                    df_query=df_query,
                    df_target=df_target,
                    field_name=field_name,
                    threshold=threshold,
                    threads=threads,
                    prefilter='prefilter' in similarity_metric,
                    denominator=denominator,
                    is_nucleotide=True,
                    verbose=verbose,
                    save_alignment=save_alignment,
                    filename=filename
                )
            elif similarity_metric == 'needle':
                sim_df = _needle_alignment(
                    df_query=df_query,
                    df_target=df_target,
                    field_name=field_name,
                    threshold=threshold,
                    threads=threads,
                    is_nucleotide=True,
                    verbose=verbose,
                    config=config,
                    save_alignment=save_alignment,
                    filename=filename
                )
            else:
                mssg = f'Alignment method: {similarity_metric} '
                mssg += f'not implemented for data_type: {data_type}'
                raise NotImplementedError(mssg)
        elif (data_type.lower() == 'smiles' or
              ('molecule' in data_type.lower() and
               'small' in data_type.lower())):
            if similarity_metric == 'fingerprint':
                print('Warning: Using `ecfp` fingerprint by default')
                similarity_metric = 'ecfp'
            if similarity_metric == 'scaffold':
                sim_df = _scaffold_alignment(
                    df_query=df_query,
                    df_target=df_target,
                    field_name=field_name,
                    threads=threads,
                    verbose=verbose,
                    save_alignment=save_alignment,
                    filename=filename
                )
            elif similarity_metric.lower() in SUPPORTED_FPS:
                sim_df = _fingerprint_alignment(
                    df_query=df_query,
                    df_target=df_target,
                    threshold=threshold,
                    field_name=field_name,
                    distance=distance,
                    threads=threads,
                    verbose=verbose,
                    bits=bits,
                    radius=radius,
                    fingerprint=similarity_metric,
                    save_alignment=save_alignment,
                    filename=filename
                )
            else:
                mssg = f'Alignment method: {similarity_metric} '
                mssg += f'not implemented for data_type: {data_type}.'
                mssg += "Please use one of the following "
                mssg += f"{', '.join(SUPPORTED_FPS)}"
                raise NotImplementedError(mssg)

        else:
            raise NotImplementedError(mssg2)
    return sim_df


def _scaffold_alignment(
    df_query: pd.DataFrame,
    df_target: pd.DataFrame = None,
    field_name: str = 'smiles',
    threads: int = cpu_count(),
    verbose: int = 0,
    save_alignment: bool = False,
    filename: str = None
) -> Union[pd.DataFrame, np.ndarray]:
    """_summary_

    :param df_query: _description_
    :type df_query: pd.DataFrame
    :param df_target: _description_, defaults to None
    :type df_target: pd.DataFrame, optional
    :param field_name: _description_, defaults to 'smiles'
    :type field_name: str, optional
    :param threads: _description_, defaults to cpu_count()
    :type threads: int, optional
    :param verbose: _description_, defaults to 0
    :type verbose: int, optional
    :param save_alignment: _description_, defaults to False
    :type save_alignment: bool, optional
    :param filename: _description_, defaults to None
    :type filename: str, optional
    :raises ImportError: _description_
    :raises ValueError: _description_
    :raises ValueError: _description_
    :raises RuntimeError: _description_
    :return: _description_
    :rtype: Union[pd.DataFrame, np.ndarray]
    """
    try:
        from rdkit import Chem
        from rdkit.Chem.Scaffolds.MurckoScaffold import MurckoScaffoldSmiles
    except ModuleNotFoundError:
        raise ImportError("This function requires RDKit to be installed.")
    from concurrent.futures import ThreadPoolExecutor

    if (field_name not in df_query.columns):
        raise ValueError(f'{field_name} not found in query DataFrame')
    if df_target is not None and field_name not in df_target.columns:
        raise ValueError(f'{field_name} not found in target DataFrame')

    def _compute_distance(query_scaffold: str, target_scaffolds: List[str]):
        distances = []
        for target in target_scaffolds:
            if target == query_scaffold:
                distances.append(1)
            else:
                distances.append(0)
        return distances

    if df_target is None:
        df_target = df_query

    mols_query = [Chem.MolFromSmiles(smiles)
                  for smiles in df_query[field_name]]
    mols_target = [Chem.MolFromSmiles(smiles)
                   for smiles in df_target[field_name]]
    scaffolds_query = [MurckoScaffoldSmiles(mol=mol, includeChirality=True)
                       for mol in mols_query]
    scaffolds_target = [MurckoScaffoldSmiles(mol=mol, includeChirality=True)
                        for mol in mols_target]

    jobs = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for query_scafold in scaffolds_query:
            job = executor.submit(_compute_distance, query_scafold,
                                  scaffolds_target)
            jobs.append(job)

        if verbose > 1:
            pbar = tqdm(jobs)
        else:
            pbar = jobs

        proto_df = []
        for idx, job in enumerate(pbar):
            if job.exception() is not None:
                raise RuntimeError(job.exception())
            result = job.result()
            entry = [{'query': idx, 'target': idx_target, 'metric': metric}
                     for idx_target, metric in enumerate(result)]
            proto_df.extend(entry)

    df = pd.DataFrame(proto_df)
    if save_alignment:
        if filename is None:
            filename = time.time()
        df.to_csv(f'{filename}.csv.gz', index=False, compression='gzip')
    return df


def _embedding_distance(
    query_embds: np.ndarray,
    target_embds: Optional[np.ndarray] = None,
    distance: Union[str, Callable] = 'cosine',
    threads: int = cpu_count(),
    threshold: float = 0.0,
    save_alignment: bool = False,
    filename: str = None,
    to_df: bool = True,
    **kwargs
) -> pd.DataFrame:
    if target_embds is None:
        target_embds = query_embds

    bulk_sim_metric = BULK_SIM_METRICS[distance]
    chunk_size = threads * 1_000
    chunks_target = (len(target_embds) // chunk_size) + 1
    queries, targets, metrics = [], [], []
    pbar = tqdm(range(len(query_embds)))

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for chunk in pbar:
            jobs = []
            for chunk_t in range(chunks_target):
                start_t = chunk_t * chunk_size
                if chunk_t == chunks_target - 1:
                    end_t = -1
                else:
                    end_t = (chunk_t + 1) * chunk_size
                if end_t == -1:
                    chunk_fps = target_embds[start_t:]
                else:
                    chunk_fps = target_embds[start_t:end_t]

                query_fp = query_embds[chunk]
                job = executor.submit(bulk_sim_metric, query_fp, chunk_fps)
                jobs.append(job)

            for idx, job in enumerate(jobs):
                if job.exception() is not None:
                    raise RuntimeError(job.exception())
                result = job.result()
                for idx_target, metric in enumerate(result):
                    if metric < threshold:
                        continue
                    queries.append(int(chunk))
                    targets.append(int((idx * chunk_size) + idx_target))
                    metrics.append(metric)

    df = pd.DataFrame({'query': queries, 'target': targets,
                       'metric': metrics})
    if distance not in ['cosine-np']:
        df.metric = df.metric.map(lambda x: 1 / (1 + x))

    df = df[df['metric'] > threshold]
    if save_alignment:
        if filename is None:
            filename = time.time()
        df.to_csv(f'{filename}.csv.gz', index=False, compression='gzip')
    return df


def _fingerprint_alignment(
    df_query: pd.DataFrame,
    df_target: pd.DataFrame = None,
    threshold: float = 0.0,
    field_name: str = 'smiles',
    distance: str = 'tanimoto',
    threads: int = cpu_count(),
    verbose: int = 0,
    bits: int = 1024,
    radius: int = 2,
    save_alignment: bool = False,
    fingerprint: str = 'ecfp', 
    filename: str = None,
    **kwargs
) -> pd.DataFrame:

    from tqdm.contrib.concurrent import thread_map
    try:
        from rdkit import Chem
        from rdkit.Chem import rdFingerprintGenerator, rdMolDescriptors
        from rdkit.DataStructs import (
            BulkTanimotoSimilarity, BulkDiceSimilarity,
            BulkSokalSimilarity, BulkRogotGoldbergSimilarity,
            BulkCosineSimilarity
        )
    except ModuleNotFoundError:
        raise ImportError("This function requires RDKit to be installed.")

    BULK_SIM_METRICS.update({
        'tanimoto': BulkTanimotoSimilarity,
        'dice': BulkDiceSimilarity,
        'sokal': BulkSokalSimilarity,
        'rogot-goldberg': BulkRogotGoldbergSimilarity,
        'cosine': BulkCosineSimilarity
    })

    if fingerprint == 'ecfp':
        fpgen = rdFingerprintGenerator.GetMorganGenerator(
            radius=radius, fpSize=bits
        )

        def _get_fp(smile: str):
            mol = Chem.MolFromSmiles(smile)
            if distance in ['dice', 'tanimoto', 'sokal', 'rogot-goldberg',
                            'cosine']:
                fp = fpgen.GetFingerprint(mol)
            else:
                fp = fpgen.GetFingerprintAsNumPy(mol).astype(np.int8)
            return fp
    elif fingerprint == 'maccs':

        def _get_fp(smile: str):
            mol = Chem.MolFromSmiles(smile)
            if distance in ['dice', 'tanimoto', 'sokal', 'rogot-goldberg',
                            'cosine']:
                fp = rdMolDescriptors.GetMACCSKeysFingerprint(mol)
            else:
                fp = fpgen.GetFingerprintAsNumPy(mol).astype(np.int8)
            return fp
    elif fingerprint == 'mapc':
        try:
            from mapchiral.mapchiral import encode
        except ModuleNotFoundError:
            raise ImportError('This fingerprint requires mapchiral to be installed.')

        def _get_fp(smile: str):
            mol = Chem.MolFromSmiles(smile, sanitize=True)
            fp = encode(mol, max_radius=radius,
                        n_permutations=bits, mapping=False)
            return fp


        if distance != 'jaccard':
            raise ValueError('MAPc can only be used with `jaccard`.')

    if distance in BULK_SIM_METRICS:
        bulk_sim_metric = BULK_SIM_METRICS[distance]
    else:
        raise NotImplementedError(
            f'Distance metric: {distance} not implemented. ' +
            f"Supported metrics: {', '.join(BULK_SIM_METRICS.keys())}"
        )

    def _parallel_fps(mols: List[str], mssg: str) -> list:
        fps = []
        jobs = []
        with ThreadPoolExecutor(max_workers=threads) as executor:
            for mol in mols:
                job = executor.submit(_get_fp, mol)
                jobs.append(job)
            pbar = tqdm(jobs, desc=mssg)
            for job in pbar:
                if job.exception() is not None:
                    raise RuntimeError(job.exception())
                result = job.result()
                fps.append(result)
        pbar.close()
        return fps

    if (field_name not in df_query.columns):
        raise ValueError(f'{field_name} not found in query DataFrame')
    if df_target is not None and field_name not in df_target.columns:
        raise ValueError(f'{field_name} not found in target DataFrame')

    if verbose > 1:
        print(f'Calculating molecular similarities using {fingerprint}-{radius * 2}',
              f'with {bits:,} bits and {distance} index...')\

    query_mols = df_query[field_name].tolist()
    chunk_size = threads * 1_000
    query_fps = _parallel_fps(query_mols, 'Query FPs')

    if df_target is None:
        df_target = df_query
        target_fps = query_fps
    else:
        target_fps = _parallel_fps(df_target[field_name], 'Target FPs')

    if fingerprint == 'mapc':
        query_fps = np.stack(query_fps)
        target_fps = np.stack(target_fps)
    if isinstance(query_fps, np.ndarray):
        max_complex = query_fps.shape[0] * target_fps.shape[0]
        query_size = query_fps.shape[0]
    else:
        max_complex = len(query_fps) * len(target_fps)
        query_size = len(query_fps)

    chunks_target = (len(df_target) // chunk_size) + 1
    metrics = np.zeros((max_complex), dtype=np.float16)

    if max_complex < 1e5:
        index_type = np.uint16
    elif max_complex < 1e9:
        index_type = np.uint32
    elif max_complex < 1e19:
        index_type = np.uint64
    else:
        index_type = np.uint128

    queries = np.zeros_like(metrics, dtype=index_type)
    targets = np.zeros_like(metrics, dtype=index_type)
    if verbose > 1:
        print()
        pbar = tqdm(range(query_size), desc='Similarity calculation')
    else:
        pbar = range(query_size)

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for chunk in pbar:
            jobs = []
            for chunk_t in range(chunks_target):
                start_t = chunk_t * chunk_size
                if chunk_t == chunks_target - 1:
                    end_t = -1
                else:
                    end_t = (chunk_t + 1) * chunk_size
                if end_t == -1:
                    chunk_fps = target_fps[start_t:]
                else:
                    chunk_fps = target_fps[start_t:end_t]

                query_fp = query_fps[chunk]

                job = executor.submit(bulk_sim_metric, query_fp, chunk_fps)
                jobs.append(job)

            for idx, job in enumerate(jobs):
                if job.exception() is not None:
                    raise RuntimeError(job.exception())
                result = job.result()
                for idx_target, metric in enumerate(result):
                    target_pointer = int((idx * chunk_size) + idx_target)
                    query_pointer = int(chunk)
                    pointer = (query_pointer * query_size) + target_pointer
                    if metric < threshold:
                        continue
                    queries[pointer] = query_pointer
                    targets[pointer] = target_pointer
                    metrics[pointer] = metric

    mask = metrics > threshold
    queries = queries[mask]
    targets = targets[mask]
    metrics = metrics[mask]

    df = pd.DataFrame({'query': queries, 'target': targets, 'metric': metrics})
    df = df[df['metric'] > threshold]
    if save_alignment:
        if filename is None:
            filename = time.time()
        df.to_csv(f'{filename}.csv.gz', index=False, compression='gzip')
    return df


def _foldseek_alignment(
    df_query: pd.DataFrame,
    df_target: pd.DataFrame = None,
    field_name: str = 'structure',
    threshold: float = 0.0,
    prefilter: bool = True,
    denominator: str = 'shortest',
    representation: str = '3di+aa',
    threads: int = cpu_count(),
    verbose: int = 0,
    save_alignment: bool = False,
    filename: str = None,
    **kwargs
) -> Union[pd.DataFrame, np.ndarray]:
    """_summary_

    :param df_query: _description_
    :type df_query: pd.DataFrame
    :param df_target: _description_, defaults to None
    :type df_target: pd.DataFrame, optional
    :param field_name: _description_, defaults to 'structure'
    :type field_name: str, optional
    :param threshold: _description_, defaults to 0.0
    :type threshold: float, optional
    :param prefilter: _description_, defaults to True
    :type prefilter: bool, optional
    :param denominator: _description_, defaults to 'shortest'
    :type denominator: str, optional
    :param representation: _description_, defaults to '3di+aa'
    :type representation: str, optional
    :param threads: _description_, defaults to cpu_count()
    :type threads: int, optional
    :param verbose: _description_, defaults to 0
    :type verbose: int, optional
    :param save_alignment: _description_, defaults to False
    :type save_alignment: bool, optional
    :param filename: _description_, defaults to None
    :type filename: str, optional
    :raises ImportError: _description_
    :raises ValueError: _description_
    :raises ValueError: _description_
    :return: _description_
    :rtype: Union[pd.DataFrame, np.ndarray]
    """
    foldseek = os.path.join(os.path.dirname(__file__), '..',
                            'bin', 'foldseek')
    if os.path.exists(foldseek):
        pass
    elif shutil.which('foldseek') is None:
        mssg = "Foldseek not found. Please install following the instructions"
        mssg += " in: https://github.com/IBM/Hestia-OOD#installation"
        raise ImportError(mssg)
    else:
        foldseek = 'foldseek'

    from hestia.utils import _collect_pdb_files

    if (field_name not in df_query.columns):
        raise ValueError(f'{field_name} not found in query DataFrame')
    if df_target is not None and field_name not in df_target.columns:
        raise ValueError(f'{field_name} not found in target DataFrame')

    ALIGNMENT_DICT = {'3di': '0', 'TM': '1', '3di+aa': '2'}
    DENOMINATOR_DICT = {'n_aligned': '0', 'shortest': '1', 'longest': '2'}

    if df_target is None:
        df_target = df_query
    tmp_dir = f'hestia_tmp_{time.time()}'
    if os.path.isdir(tmp_dir):
        shutil.rmtree(tmp_dir)
    os.mkdir(tmp_dir)
    if verbose > 2:
        mmseqs_v = 3
    else:
        mmseqs_v = verbose
    if verbose > 0:
        if prefilter:
            print('Calculating pairwise alignments using Foldseek',
                  'algorithm with prefilter...')
        else:
            print('Calculating pairwise alignments using Foldseek',
                  'algorithm...')
    db_query_dir = os.path.join(tmp_dir, 'query_dir')
    db_query = os.path.join(tmp_dir, 'query_db')
    db_target_dir = os.path.join(tmp_dir, 'target_dir')
    db_target = os.path.join(tmp_dir, 'target_db')
    alignment_db = os.path.join(tmp_dir, 'align_db')
    alignment_csv = os.path.join(tmp_dir, 'align_db.csv')

    if os.path.isdir(db_query_dir):
        shutil.rmtree(db_query_dir)
    if os.path.isdir(db_target_dir):
        shutil.rmtree(db_target_dir)
    os.mkdir(db_query_dir)
    os.mkdir(db_target_dir)

    _collect_pdb_files(df_query[field_name], db_query_dir)
    _collect_pdb_files(df_target[field_name], db_target_dir)

    subprocess.run([foldseek, 'createdb', db_query_dir, db_query,
                    '-v',  str(mmseqs_v)])
    subprocess.run([foldseek, 'createdb', db_target_dir, db_target,
                    '-v',  str(mmseqs_v)])
    denominator = DENOMINATOR_DICT[denominator]
    representation = ALIGNMENT_DICT[representation]
    prefilter = '0' if prefilter else '2'

    subprocess.run([foldseek, 'search', db_query, db_target, alignment_db,
                    'tmp', '-s', '9.5', '-a', '-e', 'inf',
                    '--seq-id-mode', denominator, '--threads',
                    str(threads), '--alignment-type', representation,
                    '--prefilter-mode', prefilter, '-v', str(mmseqs_v)
                    ])
    subprocess.run([foldseek, 'convertalis', db_query, db_target,
                    alignment_db, alignment_csv, '--format-mode', '4',
                    '--threads', str(threads), '--format-output',
                    'query,target,fident,alnlen,qlen,tlen,prob,alntmscore',
                    '-v', str(mmseqs_v)])

    df = pd.read_csv(alignment_csv, sep='\t')
    qry2idx = {os.path.basename(qry).split('.pdb')[0]: idx for idx, qry in
               enumerate(df_query[field_name].unique())}
    tgt2idx = {os.path.basename(tgt).split('.pdb')[0]: idx for idx, tgt in
               enumerate(df_target[field_name].unique())}

    if save_alignment:
        if filename is None:
            filename = time.time()
        df.to_csv(f'{filename}.csv.gz', index=False, compression='gzip')

    if representation.lower() == 'tm':
        df['metric'] = df['alntmscore']
    else:
        df['metric'] = df['prob']

    df['query'] = df['query'].map(lambda x: qry2idx[
        x.split('.pdb')[0].split('_')[0]])
    df['query'] = df['query'].astype(int)
    df['target'] = df['target'].map(lambda x: tgt2idx[
        x.split('.pdb')[0].split('_')[0]])
    df['target'] = df['target'].astype(int)
    df = df[df['metric'] > threshold]
    shutil.rmtree(tmp_dir)
    return df


def _mmseqs2_alignment(
    df_query: pd.DataFrame,
    df_target: pd.DataFrame = None,
    field_name: str = 'sequence',
    threshold: float = 0.0,
    prefilter: bool = True,
    denominator: str = 'shortest',
    threads: int = cpu_count(),
    is_nucleotide: bool = False,
    verbose: int = 0,
    save_alignment: bool = False,
    filename: str = None
) -> Union[pd.DataFrame, np.ndarray]:
    """_summary_

    :param df_query: _description_
    :type df_query: pd.DataFrame
    :param df_target: _description_, defaults to None
    :type df_target: pd.DataFrame, optional
    :param field_name: _description_, defaults to 'sequence'
    :type field_name: str, optional
    :param threshold: _description_, defaults to 0.0
    :type threshold: float, optional
    :param prefilter: _description_, defaults to True
    :type prefilter: bool, optional
    :param denominator: _description_, defaults to 'shortest'
    :type denominator: str, optional
    :param threads: _description_, defaults to cpu_count()
    :type threads: int, optional
    :param is_nucleotide: _description_, defaults to False
    :type is_nucleotide: bool, optional
    :param verbose: _description_, defaults to 0
    :type verbose: int, optional
    :param save_alignment: _description_, defaults to False
    :type save_alignment: bool, optional
    :param filename: _description_, defaults to None
    :type filename: str, optional
    :raises RuntimeError: _description_
    :raises ValueError: _description_
    :raises ValueError: _description_
    :return: _description_
    :rtype: Union[pd.DataFrame, np.ndarray]
    """
    if shutil.which('mmseqs') is None:
        raise RuntimeError(
            "MMSeqs2 not found. Please install following the instructions in:",
            "https://github.com/IBM/Hestia-OOD#installation"
        )
    from hestia.utils.file_format import _write_fasta

    if (field_name not in df_query.columns):
        raise ValueError(f'{field_name} not found in query DataFrame')
    if df_target is not None and field_name not in df_target.columns:
        raise ValueError(f'{field_name} not found in target DataFrame')

    DENOMINATOR_DICT = {'n_aligned': '0', 'shortest': '1', 'longest': '2'}

    tmp_dir = f'hestia_tmp_{time.time()}'
    if os.path.isdir(tmp_dir):
        shutil.rmtree(tmp_dir)
    os.mkdir(tmp_dir)

    if verbose > 2:
        mmseqs_v = 3
    else:
        mmseqs_v = verbose

    if verbose > 0:
        if prefilter:
            print('Calculating pairwise alignments using MMSeqs2 algorithm',
                  'with prefilter...')
        else:
            print('Calculating pairwise alignments using MMSeqs2 algorithm...')

    if df_target is None:
        df_target = df_query

    db_query_file = os.path.join(tmp_dir, 'db_query.fasta')
    db_target_file = os.path.join(tmp_dir, 'db_target.fasta')
    _write_fasta(df_query[field_name].tolist(), df_query.index.tolist(),
                 db_query_file)
    _write_fasta(df_target[field_name].tolist(), df_target.index.tolist(),
                 db_target_file)

    dbtype = '2' if is_nucleotide else '1'
    subprocess.run(['mmseqs', 'createdb', '--dbtype',
                    dbtype, db_query_file, '-v', '1',
                    f'{tmp_dir}/db_query'])
    subprocess.run(['mmseqs', 'createdb', '--dbtype',
                    dbtype, db_target_file, '-v', '1',
                    f'{tmp_dir}/db_target'])

    if is_nucleotide or prefilter:
        subprocess.run(['mmseqs', 'prefilter', '-s',
                        '6', f'{tmp_dir}/db_query',
                        f'{tmp_dir}/db_target',
                        f'{tmp_dir}/pref', '-v',
                        f'{mmseqs_v}'])
    else:
        program_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'utils', 'mmseqs_fake_prefilter.sh'
        )
        subprocess.run([program_path,
                        f'{tmp_dir}/db_query', f'{tmp_dir}/db_target',
                        f'{tmp_dir}/pref', 'db_query'])

    denominator = DENOMINATOR_DICT[denominator]
    subprocess.run(['mmseqs', 'align',  f'{tmp_dir}/db_query',
                    f'{tmp_dir}/db_target', f'{tmp_dir}/pref',
                    f'{tmp_dir}/align_db', '--alignment-mode', '3',
                    '-e', '1e2', '--seq-id-mode', denominator,
                    '--cov-mode', '5', '-c', '0.7',
                    '-v', f'{mmseqs_v}', '--threads', f'{threads}'])

    file = os.path.join(tmp_dir, 'alignments.tab')
    subprocess.run(['mmseqs', 'convertalis', f'{tmp_dir}/db_query',
                    f'{tmp_dir}/db_target', f'{tmp_dir}/align_db',
                    '--format-mode', '4', '--threads', f'{threads}',
                    file, '-v', '1'])

    df = pd.read_csv(file, sep='\t')
    df['metric'] = df['fident']
    df = df[df['metric'] > threshold]
    df = df[['query', 'target', 'metric']]
    if save_alignment:
        if filename is None:
            filename = time.time()
        df.to_csv(f'{filename}.csv.gz', index=False, compression='gzip')

    shutil.rmtree(tmp_dir)
    return df


def _needle_alignment(
    df_query: pd.DataFrame,
    df_target: pd.DataFrame = None,
    field_name: str = 'sequence',
    threshold: float = 0.0,
    denominator: str = 'shortest',
    threads: int = cpu_count(),
    is_nucleotide: bool = False,
    verbose: int = 0,
    config: dict = None,
    save_alignment: bool = False,
    filename: str = None
):
    """_summary_

    :param df_query: _description_
    :type df_query: pd.DataFrame
    :param df_target: _description_, defaults to None
    :type df_target: pd.DataFrame, optional
    :param field_name: _description_, defaults to 'sequence'
    :type field_name: str, optional
    :param threshold: _description_, defaults to 0.0
    :type threshold: float, optional
    :param denominator: _description_, defaults to 'shortest'
    :type denominator: str, optional
    :param threads: _description_, defaults to cpu_count()
    :type threads: int, optional
    :param is_nucleotide: _description_, defaults to False
    :type is_nucleotide: bool, optional
    :param verbose: _description_, defaults to 0
    :type verbose: int, optional
    :param config: _description_, defaults to None
    :type config: dict, optional
    :param save_alignment: _description_, defaults to False
    :type save_alignment: bool, optional
    :param filename: _description_, defaults to None
    :type filename: str, optional
    :raises ImportError: _description_
    :raises ValueError: _description_
    :raises ValueError: _description_
    :raises RuntimeError: _description_
    :return: _description_
    :rtype: _type_
    """
    if shutil.which("needleall") is None:
        raise ImportError("EMBOSS needleall not found. Please install by ",
                          "running: `conda install emboss -c bioconda`")
    from hestia.utils.file_format import _write_fasta_chunks
    from concurrent.futures import ThreadPoolExecutor

    if (field_name not in df_query.columns):
        raise ValueError(f'{field_name} not found in query DataFrame')
    if df_target is not None and field_name not in df_target.columns:
        raise ValueError(f'{field_name} not found in target DataFrame')

    if config is None:
        config = {
            "gapopen": 10,
            "gapextend": 0.5,
            "endweight": True,
            "endopen": 10,
            "endextend": 0.5,
            "matrix": "EBLOSUM62"
        }

    tmp_dir = f"hestia_tmp_{time.time()}"
    db_query = os.path.join(tmp_dir, 'db_query')
    db_target = os.path.join(tmp_dir, 'db_target')
    if os.path.isdir(tmp_dir):
        shutil.rmtree(tmp_dir)
    os.mkdir(tmp_dir)
    os.mkdir(db_query)
    os.mkdir(db_target)

    if df_target is None:
        df_target = df_query

    n_query = len(df_query)
    df_query['tmp_id'] = [i for i in range(n_query)]
    df_target['tmp_id'] = [j + n_query for j in range(len(df_target))]

    all_seqs = df_query[field_name].tolist() + df_target[field_name].tolist()
    query_id2idx = {s_id: idx for idx, s_id
                    in enumerate(df_query.tmp_id)}
    target_idx2id = {s_id: idx for idx, s_id
                     in enumerate(df_target.tmp_id)}
    all_ids = sorted(query_id2idx.keys()) + sorted(target_idx2id.keys())
    seq_lengths = {str(s_id): len(seq) for s_id, seq in zip(all_ids, all_seqs)}
    del all_seqs, all_ids
    jobs_query = _write_fasta_chunks(df_query[field_name].tolist(),
                                     df_query.tmp_id.tolist(),
                                     threads, db_query)
    jobs_target = _write_fasta_chunks(df_target[field_name].tolist(),
                                      df_target.tmp_id.tolist(),
                                      threads, db_target)
    jobs = []
    proto_df = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for i in range(jobs_query):
            for j in range(jobs_target):
                query = os.path.join(db_query, f"{i}.fasta.tmp")
                target = os.path.join(db_target, f"{j}.fasta.tmp")
                job = executor.submit(_compute_needle, query, target,
                                      threshold, denominator, is_nucleotide,
                                      seq_lengths, **config)
                jobs.append(job)

        if verbose > 1:
            pbar = tqdm(jobs)
        else:
            pbar = jobs

        for job in pbar:
            if job.exception() is not None:
                raise RuntimeError(job.exception())

            result = job.result()
            for query, target, metric in result:
                entry = {
                    'query': query_id2idx[int(query)],
                    'target': target_idx2id[int(target)],
                    'metric': metric
                }
                proto_df.append(entry)

    df = pd.DataFrame(proto_df)
    if save_alignment:
        if filename is None:
            filename = time.time()
        df.to_csv(f'{filename}.csv.gz', index=False, compression='gzip')
    shutil.rmtree(tmp_dir)
    df = df[df['metric'] > threshold]
    return df


def _compute_needle(
    query: str,
    target: str,
    threshold: float,
    denominator: str,
    is_nucleotide: bool,
    seq_lengths: dict,
    gapopen: float = 10,
    gapextend: float = 0.5,
    endweight: bool = True,
    endopen: float = 10,
    endextend: float = 0.5,
    matrix: str = 'EBLOSUM62'
):
    if is_nucleotide:
        type_1, type_2, = '-snucleotide1', '-snucleotide2'
    else:
        type_1, type_2 = '-sprotein1', '-sprotein2'

    FIDENT_CALCULATION = {
        'n_aligned': lambda x: float(x.split('(')[1][:-3])/100,
        'shortest': lambda x, q, t: int(x[11:].split('/')[0]) / min(q, t),
        'longest': lambda x, q, t: int(x[11:].split('/')[0]) / max(q, t)
    }[denominator]

    command = ["needleall", "-auto", "-stdout",
               "-aformat", "pair",
               "-gapopen", str(gapopen),
               "-gapextend", str(gapextend),
               "-endopen", str(endopen),
               "-endextend", str(endextend),
               "-datafile", matrix,
               type_1, type_2, query, target]

    if endweight:
        command.append("-endweight")

    result = []

    with subprocess.Popen(
        command, stdout=subprocess.PIPE,
        bufsize=1, universal_newlines=True
    ) as process:
        for idx, line in enumerate(process.stdout):
            if line.startswith('# 1:'):
                query = line[5:].split()[0].split('|')[0]

            elif line.startswith('# 2:'):
                target = line[5:].split()[0].split('|')[0]

            elif line.startswith('# Identity:'):
                fident = FIDENT_CALCULATION(
                    line, seq_lengths[query],
                    seq_lengths[target]
                )
            elif line.startswith('# Gaps:'):
                if (fident < threshold or query == target):
                    continue
                result.append((query, target, fident))
    return result
