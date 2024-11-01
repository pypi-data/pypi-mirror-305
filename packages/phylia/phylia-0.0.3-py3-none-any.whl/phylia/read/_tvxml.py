
import os
import lxml.etree as ET
from pandas import Series, DataFrame
import pandas as pd

from .._core._releve import Releve

class TvXml:
    """Read Turboveg XML file."""
    
    def __init__(self, tree):
        """
        Parameters
        ----------
        tree : ElementTree tree object
            Valid XML tree with Turboveg releve dataset.

        Notes
        -----
        Use .from_xml method for creating TvXml instance from XML files.
        ...
        """
        self._tree = tree
        self._root = self._tree.getroot()
        self.xmlinfo = Series(self._root.attrib, name='xmlinfo')

    def __repr__(self):
        return f'{self.__class__.__name__}(n={len(self)}'

    def __len__(self):
        return len(self.guids)

    @classmethod
    def from_file(cls,xmlpath):
        """Read Turboveg XML file.

        Parameters
        ----------
        xmlpath : str
            Valid filepath to XML file with groundwater level measurements.

        Returns
        -------
        TvXml object

        Example
        -------
        tvxml = TvXml.from_file(<valid xml filepath>)
        """

        if not os.path.isfile(xmlpath):
            raise ValueError(f'Invalid filepath: "{xmlpath}".')
        tree = ET.parse(xmlpath)
        return cls(tree)

    @property
    def lookuptables(self):
        """Return dictionary with available lookuptables."""
        tables = {}
        for tablename in self.lookuptablenames:
            if tablename=='Coverscale_list':
                # Coverscale_list may contain nested lists because a 
                # dataset may contain multiple coverscales
                tables[tablename] = self.get_coverscales()
            else:
                items = []
                for rec in self._tree.find(f".//{tablename}").iterchildren():
                    items.append(dict(zip(rec.keys(),rec.values())))
                tables[tablename] = DataFrame(items)
        return tables

    @property
    def lookuptablenames(self):
        """Return list of names of available lookuptables."""
        return [table.tag for table in self._tree.find(".//Lookup_tables").iterchildren()]

    def get_lookuptable(self,name):
        """Return lookuptable by name.
        
        Parameters
        ----------
        name : string
            Lookup tablename (as returned by lookupnames).
            If name is not a valid lookup tablename, all tables are
            returned.

        Returns
        -------
        pd.DataFrame
        """
        try:
            return self.lookuptables[name]
        except KeyError as e_info:
            raise KeyError(f'No lookuptable with name "{name}" in dictionary of lookuptables.')

    @property
    def guids(self):
        """Return list of unique releve identifier (guid) for each releve."""
        return list(self.tvhabita.index.values)

    @property
    def tvflora(self):
        """Return species table."""
        tbl = self.get_lookuptable('Species_list')
        tbl['nr'] = tbl['nr'].astype('int64')
        tbl['valid_nr'] = tbl['valid_nr'].astype('int64')
        tbl = tbl.set_index('nr',drop=True).sort_values('name')
        tbl.index.name = 'species_nr'
        return tbl

    @property
    def guidnumbers(self):
        """Return unique numbers for guids."""
        guids = []
        for plot in self._root.iterfind('.//Plot'):
            guid = plot.attrib['guid'].strip('{').strip('}')
            guids.append(guid)
        relnrs = list(range(1,len(guids)+1))
        return Series(relnrs, index=guids, name='relnrs')

    @property
    def tvhabita(self):
        """Turboveg2 standard header data."""

        #releves = []
        # get header data for all Plots
        """
        for plot in self._root.iterfind('.//Plot'):
            # standard records
            hd = Series(plot.find(".//header_data//standard_record").attrib)
            hd = DataFrame(hd).T
            # user defined records
            for rec in plot.iterfind(".//header_data//udf_record"):
                hd[rec.attrib['name']] = rec.attrib['value']
            releves.append(hd)
        tvhab = pd.concat(releves)
        """
        releves = []
        for plot in self._root.iterfind('.//Plot'):

            plot_attributes = {}

            # plot identifiers
            for key in ['guid','database','releve_nr',]:
                value = plot.attrib[key]
                if key=='guid':
                    value = value.strip('{').strip('}')
                plot_attributes[key] = value
            
            # standard attributes
            standard_attributes = plot.find(".//header_data//standard_record").attrib
            for key in standard_attributes:
                plot_attributes[key] = standard_attributes[key]
            
            # user defined records
            for rec in plot.iterfind(".//header_data//udf_record"):
                plot_attributes[rec.attrib['name']] = rec.attrib['value']

            releves.append(plot_attributes.copy())
        tvhab = DataFrame(releves)

        # convert columns dtypes
        for colname in tvhab.columns:
            template = self.tvhabita_template.loc[colname,:]
            if (template['field_type']=='N'): 
                if (template['field_dec']=='0'):
                    tvhab[colname] = tvhab[colname].astype('Int64')
                else:
                    tvhab[colname] = tvhab[colname].astype('float64')

        # conver releve id
        tvhab['releve_nr'] = tvhab['releve_nr'].astype('Int64')

        # set guid as index
        tvhab = tvhab.set_index('guid', drop=True)

        return tvhab

    @property
    def tvabund(self):
        """Species abundance data."""
        releves = []
        for plot in self._root.iterfind('.//Plot'):

            species = []
            for spec in plot.iterfind(".//species_data//species//standard_record"):
                species.append({
                    'guid' : plot.attrib['guid'].strip('{').strip('}'),
                    'database': plot.attrib['database'],
                    'releve_nr' : plot.attrib['releve_nr'],
                    'species_nr' : spec.attrib['nr'],
                    'cover_code' : spec.attrib['cover'],
                    'layer' : spec.attrib['layer'],
                    })
            releves.append(DataFrame(species))

        releves = pd.concat(releves, ignore_index=True)
        for colname in ['releve_nr','species_nr',]:
            releves[colname] = releves[colname].astype('int64')
        return releves

    @property
    def tvhabita_template(self):
        """Return header columns definitions."""

        # table of releve identifiers
        identifiers = [
            {'field_name':'guid','field_type':'C','field_len':40, 'field_dec':0, 
            'field_desc':'Unique releve identifier','ispredefined':'true',},
            {'field_name':'database','field_type':'C','field_len':200, 'field_dec':0, 
            'field_desc':'Turboveg3 source database','ispredefined':'true',},
            #{'field_name':'releve_nr','field_type':'N','field_len':10, 'field_dec':0, 
            #'field_desc':'Releve number in tv3 database','ispredefined':'true',},
            ]
        relid = DataFrame(identifiers).set_index('field_name')

        # table of turboveg predefined columns
        tvcol = self.templates['tvhabita']
        tvcol['ispredefined'] = 'true'
        
        # table of user defined (udf) header columns
        data = []
        for releve in self._tree.findall(".//Plot/header_data"):
            for rec in releve.iterchildren():
                if rec.tag!='udf_record':
                    continue
                data.append({
                    'field_name' : rec.attrib['name'],
                    'field_type' : rec.attrib['type'],
                    'field_len' : int(rec.attrib['len']),
                    'field_dec': int(rec.attrib['dec']),
                    'ispredefined':rec.attrib['ispredefined'],
                    })
                    
        colnames = data[0].keys()
        udf = DataFrame.from_records(data,columns=colnames)
        udf = udf.drop_duplicates().set_index('field_name',drop=True)

        return pd.concat([relid,tvcol,udf])


    @property
    def releve_metadata(self):
        """Releve database metadata."""
        metadata = []
        for plot in self._root.iterfind('.//Plot'):
            releve = Series(plot.attrib)
            metadata.append(DataFrame(releve).T)
        metadata = pd.concat(metadata)

        metadata['releve_nr'] = metadata['releve_nr'].astype('int64')
        metadata.set_index('guid', drop=True, inplace=True, verify_integrity=True)

        return metadata

    def get_coverscales(self,scalecode='all'):
        """Return table of coverscale definitons.
        
        Parameters
        ----------
        scalecode : str, default 'all'
            Return only coverscale with given code. If coverscalecode is 
            given that does not exist, all scales are returned.

        Returns
        -------
        pd.Dataframe
        ...
        """
        for scale in self._tree.findall(".//coverscale_record"):

            #parse coverscale
            code = scale.find("code").text
            desc = scale.find("description").text
            vals = []
            for rec in scale.iterchildren():
                if rec.tag != 'data_record':
                    continue
                coverscale = {
                    'scalecode':code,
                    'scaledescription':desc,
                    'covercode':rec.attrib['code'],
                    'cover':rec.attrib['percentage'],}
                vals.append(coverscale.copy())

        # merge all scales in one dataframe
        scales =  DataFrame(vals)

        if scalecode in scales['scalecode'].unique():
            return scales[scales['scalecode']==scalecode]
        return scales

    @property
    def _template_files(self):
        """Lookuptable filenames."""
        items = []
        for rec in self._tree.find(".//Template/Files").iterchildren():
            items.append(dict(zip(rec.keys(),rec.values())))
        return DataFrame(items).set_index('file_nr',drop=True)


    @property
    def _template_fields(self):
        """Database table definitions."""
        items = []
        for rec in self._tree.find(".//Template/Dbasedic").iterchildren():
            items.append(dict(zip(rec.keys(),rec.values())))
        return DataFrame(items)

    @property
    def templates(self):
        """Dictionary of Turboveg2 table definitions."""
        filedict = {}
        for filenumber in range(len(self._template_files)):
            tbl = self._template_fields
            tbl = tbl[tbl['file_nr']==f'{str(filenumber+1)}'].copy()
            tbl['field_name'] = tbl['field_name'].str.lower()

            filename = self._template_files.at[str(filenumber+1),'file_name']
            field_names = ['field_name','field_type','field_len','field_dec','field_desc',]
            filedict[filename] = tbl[field_names].set_index('field_name',drop=True)

        return filedict

    def get_releve(self, guid):
        """Return releve by number."""

        releve = Releve()

        # get species names
        species_nrs = self.tvabund['species_nr'].values
        mask = self.tvflora.index.isin(species_nrs)
        tvflora = self.tvflora[mask].copy()

        # species data
        releve.tvflora.reindex(tvflora.index)
        releve.tvflora['lettercode'] = tvflora['code']
        releve.tvflora['shortname'] = tvflora['name']
        releve.tvflora['abbreviat'] = tvflora['author']
        releve.tvflora['nativename'] = tvflora['nativename']
        
        # select tvhabita data and copy to series
        tvhabita = self.tvhabita.loc[guid,:]
        for (field,value) in tvhabita.items():
            releve.tvhabita[field] = value
        releve.tvhabita['releve_nr'] = guid

        # tvabund data
        tvabund = self.tvabund[self.tvabund['guid']==guid]
        releve.tvabund = pd.concat([releve.tvabund, tvabund,]).reset_index(drop=True)

        return releve
